# Website image copies

Publish using `sync.ps1` as before. The image-export step now creates smaller website copies automatically. Vault attachments are read only and are never resized or overwritten.

- Photographs: up to 2,560 pixels on the longest side, JPEG quality 85.
- Maps, surveys, diagrams, PNG graphics and document-like images: up to 6,000 pixels on the longest side, with JPEG quality 90 where applicable.
- Transparency is preserved. GIFs and animations are copied unchanged.
- Existing image filenames and links remain the same. An already smaller original is retained rather than enlarged.
- The ignored `.cache/web-images.json` file caches results and records source/output checksums. Changed originals are processed again on the next publish.

Install `requirements.txt` into the publishing Python environment if needed. On this laptop, the exporter can also use the Pillow installation bundled with Codex.

Website images are reading previews; use the original vault attachment for full-resolution survey details.
