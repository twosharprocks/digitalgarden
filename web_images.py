"""Build cached, smaller website images without modifying vault originals."""
import argparse
import hashlib
import json
import os
import re
import shutil
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import unquote

from PIL import Image, ImageOps

# The known Cocklebiddy survey scans exceed Pillow's default pixel threshold.
# Keep a firm 300-megapixel ceiling and downsample JPEGs in the decoder first.
Image.MAX_IMAGE_PIXELS = 150_000_000
POLICY = 'web-previews-v1-photos2560-maps6000-jpeg85-90'
PHOTO_LIMIT = 2560
DETAIL_LIMIT = 6000
RASTER = {'.jpg', '.jpeg', '.png', '.gif'}
DETAIL_NAME = re.compile(r'map|survey|diagram|section|topo|chart|\basf\b|\bcegsa\b|\blsecr\b|\bpart\s*\d+', re.I)

def sha(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()

def signature(path):
    stat = path.stat()
    return [str(path.resolve()), stat.st_size, stat.st_mtime_ns]

def save_manifest(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix('.next')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    os.replace(temporary, path)

def detailed_references(posts):
    result = set()
    for post in posts.rglob('*.md'):
        active = None
        for line in post.read_text(encoding='utf-8-sig').splitlines():
            heading = re.match(r'^(#{1,6})\s+(.+)', line)
            if heading:
                level = len(heading[1])
                if re.search(r'map|survey|diagram|plan', heading[2], re.I):
                    active = level
                elif active is not None and level <= active:
                    active = None
            if active is not None:
                for target in re.findall(r'/images/([^\s)]+)', line):
                    result.add(Path(unquote(target)).name.casefold())
    return result

def optimize_one(source, destination, detailed=False):
    """Re-encode from the original and atomically replace only the exported copy."""
    if source.resolve() == destination.resolve():
        raise ValueError('Source must be separate from the exported destination.')
    original_sha = sha(source)
    original_size = source.stat().st_size
    record = {'policy': POLICY, 'source': signature(source), 'source_sha256': original_sha}
    temporary_dir = Path(__file__).resolve().parent / '.cache/web-image-tmp'
    temporary_dir.mkdir(parents=True, exist_ok=True)
    fd, temporary_name = tempfile.mkstemp(prefix='.web-preview-', dir=temporary_dir)
    os.close(fd)
    temporary = Path(temporary_name)
    try:
        with Image.open(source) as opened:
            original_dimensions = list(opened.size)
            original_format = opened.format
            frames = getattr(opened, 'n_frames', 1)
            if original_format != 'JPEG' and opened.width * opened.height > 90_000_000:
                raise ValueError('Non-JPEG image exceeds the safe decoding limit.')
            preserve_alpha = destination.suffix.casefold() in {'.jpg', '.jpeg'} and ('A' in opened.getbands() or 'transparency' in opened.info)
            if frames > 1 or original_format == 'GIF' or preserve_alpha:
                shutil.copyfile(source, temporary)
                kind = 'transparency-original' if preserve_alpha else 'animation-original'
                dimensions = original_dimensions
            else:
                # Decoder-side downsampling keeps very large JPEG scans manageable.
                if original_format == 'JPEG':
                    scale = min(1, DETAIL_LIMIT / max(opened.size))
                    opened.draft('RGB', (max(1, round(opened.width * scale)), max(1, round(opened.height * scale))))
                image = ImageOps.exif_transpose(opened)
                try:
                    sample = image.resize((min(128, image.width), min(128, image.height))).convert('L')
                    histogram = sample.histogram()
                    paper_like = sum(histogram[225:]) / max(1, sum(histogram)) > 0.35
                    sample.close()
                    is_detail = detailed or bool(DETAIL_NAME.search(source.stem)) or original_format == 'PNG' or paper_like or max(image.size) / max(1, min(image.size)) > 2.2
                    limit = DETAIL_LIMIT if is_detail else PHOTO_LIMIT
                    if image.mode == 'P':
                        converted = image.convert('RGBA' if 'transparency' in image.info else 'RGB')
                        image.close()
                        image = converted
                    image.thumbnail((limit, limit), Image.Resampling.LANCZOS)
                    if original_format in {'JPEG', 'PNG', 'WEBP'} and destination.suffix.casefold() in {'.jpg', '.jpeg'}:
                        if image.mode != 'RGB':
                            converted = image.convert('RGB')
                            image.close()
                            image = converted
                        options = dict(quality=90 if is_detail else 85, optimize=True, progressive=True, subsampling=0 if is_detail else 2)
                        if opened.mode == 'RGB' and opened.info.get('icc_profile'):
                            options['icc_profile'] = opened.info['icc_profile']
                        image.save(temporary, format='JPEG', **options)
                    elif original_format in {'JPEG', 'PNG', 'WEBP'} and destination.suffix.casefold() == '.png':
                        image.save(temporary, format='PNG', optimize=True)
                    else:
                        raise ValueError(f'Unsupported image format {original_format}: {source.name}')
                    dimensions = list(image.size)
                    kind = 'detail-preview' if is_detail else 'photo-preview'
                finally:
                    image.close()
        # Keep an already smaller original rather than inflating a tiny graphic.
        if temporary.stat().st_size >= original_size:
            shutil.copyfile(source, temporary)
            dimensions = original_dimensions
            kind = 'already-smaller-original'
        with Image.open(temporary) as check:
            check.verify()
        os.replace(temporary, destination)
        record.update(original_bytes=original_size, exported_bytes=destination.stat().st_size,
                      original_dimensions=original_dimensions, dimensions=dimensions,
                      kind=kind, output_sha256=sha(destination), format=original_format, detail_hint=detailed)
        return record
    finally:
        temporary.unlink(missing_ok=True)

def run(images, originals, posts, manifest_path):
    images = images.resolve()
    originals = originals.resolve()
    assert images != originals and not images.is_relative_to(originals), 'Export destination must be outside the vault originals.'
    sources = {}
    for path in originals.rglob('*'):
        if path.is_file():
            sources.setdefault(path.name.casefold(), path)
    detail = detailed_references(posts)
    manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    cache = manifest.get('files', {})
    results = {}
    tasks = []
    skipped_missing_original = []
    for destination in images.iterdir():
        if not destination.is_file() or destination.suffix.casefold() not in RASTER:
            continue
        source = sources.get(destination.name.casefold())
        if source is None:
            skipped_missing_original.append(destination.name)
            continue
        previous = cache.get(destination.name)
        hint = destination.name.casefold() in detail
        if previous and previous.get('policy') == POLICY and previous.get('detail_hint') == hint and previous.get('source') == signature(source) and previous.get('output_sha256') == sha(destination):
            results[destination.name] = previous
        else:
            tasks.append((source, destination, hint))
    print(f'[WEB IMAGES] Optimizing {len(tasks)} images; {len(results)} cached.', flush=True)
    errors = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(optimize_one, *task): task[1] for task in tasks}
        for i, future in enumerate(as_completed(futures), 1):
            destination = futures[future]
            try:
                results[destination.name] = future.result()
            except Exception as exc:
                print(f'[WEB IMAGES] ERROR {destination.name}: {exc}', flush=True)
                errors.append((destination.name, str(exc)))
            if i % 50 == 0 or i == len(tasks):
                print(f'[WEB IMAGES] {i}/{len(tasks)} processed.', flush=True)
                save_manifest(manifest_path, {'policy': POLICY, 'files': results})
    before = sum(item['original_bytes'] for item in results.values())
    after = sum(item['exported_bytes'] for item in results.values())
    save_manifest(manifest_path, {'policy': POLICY, 'files': results, 'skipped_missing_original': skipped_missing_original})
    print(f'[WEB IMAGES] {len(results)} images: {before:,} original bytes -> {after:,} exported bytes ({100 * (1-after/max(1,before)):.1f}% smaller).', flush=True)
    if skipped_missing_original:
        print(f'[WEB IMAGES] Kept {len(skipped_missing_original)} older exports unchanged; originals unavailable.', flush=True)
    if errors:
        raise RuntimeError(f'{len(errors)} image exports need attention: {errors}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('images', type=Path)
    parser.add_argument('originals', type=Path)
    parser.add_argument('posts', type=Path)
    parser.add_argument('--manifest', type=Path, default=Path(__file__).resolve().parent / '.cache/web-images.json')
    args = parser.parse_args()
    run(args.images, args.originals, args.posts, args.manifest)
