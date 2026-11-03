"""Apply private Karst decisions to website copies, leaving the vault unchanged."""
import argparse,hashlib,json,re
from pathlib import Path
HOME=Path.home()/'Documents'/'Codex';PRIVATE=HOME/'Website Publication';KARST=HOME/'Karst Sync'
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(raw):return hashlib.sha256(raw).hexdigest()
def save(p,d):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def identity(name,text):
 m=re.search(r'(?m)^cavedb:\s*["\']?(https?://[^\s"\']+)',text)
 return m[1] if m else 'name:'+name
class WebsiteRules:
 def __init__(self,vault,site):
  from attachment_privacy import fingerprints
  self.vault=Path(vault).resolve();self.site=Path(site).resolve();self.root=PRIVATE/'effective-sources';self.policy_path=PRIVATE/'website-policy.json'
  if PRIVATE.resolve().is_relative_to(self.site) or PRIVATE.resolve().is_relative_to(self.vault):raise ValueError('Private website policy location is unsafe')
  config=read(KARST/'config.json');rules=read(KARST/'policy/record-rules.json');decisions=read(PRIVATE/'decisions.json')
  summaries=read(PRIVATE/'approved-summaries.json')
  if {r['identity'] for r in rules if r['mode']=='reduced'}!=set(summaries):raise ValueError('Protected summary registry and Karst rules disagree')
  policy=read(config['shared_policy']);self.texts={};self.sources={};self.events=[];index={};self.excluded=set()
  for p in (self.vault/'1 - Published').rglob('*'):
   if p.is_symlink():raise ValueError('Published symlink requires review')
   if not p.is_file():continue
   self.sources[str(p)]=sha(p.read_bytes())
   if p.suffix.lower()!='.md':raise ValueError('Non-note in Published needs review: '+p.name)
   text=p.read_text(encoding='utf-8-sig');self.texts[str(p)]=text;index.setdefault(identity(p.stem,text),[]).append(p)
  for rule in rules:
   paths=index.get(rule['identity'],[])
   if len(paths)>1 and rule['mode']!='reduced':paths=[p for p in paths if p.stem==rule['name']]
   if len(paths)!=1:raise ValueError('Missing or ambiguous Karst publishing identity: '+rule['name'])
   p=paths[0];key=str(p);current=self.texts[key]
   if rule['mode']=='reviewed' and self.sources[key]!=rule['source_sha256']:self.events.append({'record':p.stem,'source_changed':True,'approved_copy_held_fixed':True,'review_required':True})
   if rule['mode']=='reduced':
    summaries=read(PRIVATE/'approved-summaries.json');summary=summaries[rule['identity']]
    if sha(rule['text'].encode('utf-8'))!=summary['rule_text_sha256']:raise ValueError('Karst public summary rule changed; reconcile approved website copy')
    public=(PRIVATE/'approved-summaries'/summary['file']).read_bytes()
    if sha(public)!=summary['sha256']:raise ValueError('Approved website summary changed unexpectedly')
    self.texts[key]=public.decode('utf-8')
   elif rule['mode']=='reviewed':self.texts[key]=rule['text']
   else:
    front,body=current.split('---',2)[1:];front=re.sub(r'(?m)^related:[^\n]*\n(?:[ \t]+[^\n]*\n|\n)*','',front);self.texts[key]='---'+front+'---'+body
   if rule['mode']=='reduced' and self.sources[key]!=rule['source_sha256']:self.events.append({'record':p.stem,'public_summary_held_fixed':True})
  published=read(PRIVATE/'karst-publication.json') if (PRIVATE/'karst-publication.json').exists() else {'revision':'a91711b0be35b53a5de563e070ff13f8b90c3afa','attachments':read(PRIVATE/'karst-attachment-manifest.json')}
  self.karst_revision=published['revision']
  if not re.fullmatch(r'[0-9a-f]{40}',self.karst_revision):raise ValueError('Invalid published Karst revision')
  manifest=published['attachments'];self.manifest=manifest;approved={x['source_sha256'] for x in manifest.values()};outputs={x['sha256'] for x in manifest.values()}
  omitted=read(PRIVATE/'karst-omitted-identities.json');denied_sha={x['sha256'] for x in omitted.values()};denied_git={x['git_blob_sha1'] for x in omitted.values()};self.needles=config['redacted_location_needles']
  for d in decisions:
   path=Path(d['path']);ident=fingerprints(path)
   if ident['sha256']!=d['sha256']:raise ValueError('Reviewed website attachment changed: '+path.name)
   denied_sha.add(ident['sha256']);denied_git.add(ident['git_blob_sha1'])
   for key,text in list(self.texts.items()):
    token=re.compile(r'!?\[\[\s*'+re.escape(path.name)+r'(?:\|[^\]]*)?\]\]')
    if not token.search(text):continue
    replacement='['+d['label']+']('+d['url']+')' if d.get('url') else ''
    text=token.sub(lambda _:replacement,text);text=re.sub(r'(?m)^\s*[-*]\s*$\n?','',text);self.texts[key]=text
  policy['approved_source_sha256']=sorted((set(policy['approved_source_sha256'])|approved)-denied_sha);policy['approved_output_sha256']=sorted(set(policy['approved_output_sha256'])|outputs)
  prior=read(self.policy_path) if self.policy_path.exists() else {}
  policy['private_sha256']=sorted(set(policy['private_sha256'])|set(prior.get('private_sha256',[]))|denied_sha);policy['private_git_blobs']=sorted(set(policy['private_git_blobs'])|set(prior.get('private_git_blobs',[]))|denied_git)
  cache=self.site/'.cache/web-images.json'
  if cache.exists():
   for value in read(cache).get('files',{}).values():
    if value.get('source_sha256') in set(policy['private_sha256']) and value.get('output_sha256'):policy['private_sha256'].append(value['output_sha256'])
  policy['private_sha256']=sorted(set(policy['private_sha256']));save(self.policy_path,policy);self.verify_sources()
 def text(self,path):
  key=str(Path(path).resolve())
  if key in self.excluded:return None
  if key not in self.texts:raise ValueError('Unknown effective website source: '+key)
  return self.texts[key]
 def verify_sources(self):
  for name,digest in self.sources.items():
   if sha(Path(name).read_bytes())!=digest:raise ValueError('Vault changed during website preparation')
 def verify_prepared(self):
  snapshot=read(PRIVATE/'source-review.json')
  if snapshot['source_hashes']!=self.sources:raise ValueError('Published vault notes changed after source preparation; retry the local sync')
 def check_text(self,text):
  import html
  return any(n in html.unescape(text) for n in self.needles)
 def prepare(self):
  from attachment_privacy import PrivacyGuard
  from urllib.parse import quote
  guard=PrivacyGuard(self.vault,self.site,website=True)
  if guard.check(outputs=False):raise ValueError('Effective source privacy check failed before website copy preparation')
  by_sha={v['source_sha256']:k for k,v in self.manifest.items()}
  def link_asset(match):
   embedded=bool(match[1]);target=match[2].split('|')[0]
   if Path(target).suffix.lower() in {'.jpg','.jpeg','.png','.gif'}:return match[0]
   candidates=guard.resolve_attachment(target,embedded)
   if len(candidates)!=1:return match[0]
   path=candidates[0];digest=guard.hash(path)['sha256']
   if digest not in by_sha:return match[0]
   guard.require_exportable(path)
   alias=match[2].split('|',1)[1] if '|' in match[2] else path.stem
   if alias.isdigit():alias=path.stem
   image=embedded and path.suffix.lower() in {'.webp','.svg','.heic'}
   prefix='https://raw.githubusercontent.com/twosharprocks/Karst-Database/' if image else 'https://github.com/twosharprocks/Karst-Database/blob/'
   return ('!' if image else '')+'['+alias.replace('[','\\[').replace(']','\\]')+']('+prefix+self.karst_revision+'/'+quote(by_sha[digest],safe='/')+')'
  self.root.mkdir(parents=True,exist_ok=True);expected={}
  for name,text in self.texts.items():
   if name in self.excluded:continue
   rel=Path(name).relative_to(self.vault/'1 - Published')
   if self.check_text(text):raise ValueError('Redacted location or entry URL appears in effective note: '+str(rel))
   text=re.sub(r'(!?)\[\[([^\]]+)\]\]',link_asset,text)
   expected[rel.as_posix()]=text.encode('utf-8')
  old=read(PRIVATE/'source-manifest.json') if (PRIVATE/'source-manifest.json').exists() else {}
  for rel in set(old)-set(expected):
   p=self.root/rel
   if p.is_symlink() or not p.resolve().is_relative_to(self.root):raise ValueError('Unsafe retired effective source')
   if p.exists():
    if sha(p.read_bytes())!=old[rel]:raise ValueError('Edited effective source needs review')
    p.unlink()
  for rel,raw in expected.items():
   p=self.root/rel;p.parent.mkdir(parents=True,exist_ok=True)
   if not p.exists() or p.read_bytes()!=raw:p.write_bytes(raw)
  self.verify_sources();save(PRIVATE/'source-manifest.json',{n:sha(b) for n,b in expected.items()});save(PRIVATE/'source-review.json',{'notes':len(expected),'reduced_summaries':8,'events':self.events,'source_hashes':self.sources,'withheld':[Path(p).name for p in self.excluded]})
  print(f'Website sources prepared: {len(expected)} notes; eight reduced public versions retained.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--vault',type=Path,required=True);p.add_argument('--site',type=Path,default=Path(__file__).resolve().parent);p.add_argument('--prepare',action='store_true');a=p.parse_args();plan=WebsiteRules(a.vault,a.site)
 if a.prepare:plan.prepare()
