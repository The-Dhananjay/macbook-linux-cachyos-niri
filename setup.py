#!/usr/bin/env python3
"""Read-only discovery and safe staging for an AI-assisted Linux desktop setup.

No package install, sudo, service enablement, PAM edit or session replacement occurs here.
"""
import argparse,ast,hashlib,io,json,os,platform,re,shutil,subprocess,sys,tarfile,tempfile,tokenize
from pathlib import Path
ROOT=Path(__file__).resolve().parent
STATE=ROOT/'.setup-state'
COMMANDS=['niri','noctalia','qs','systemctl','nmcli','wpctl','pactl','pw-record','ffmpeg','nautilus','kdeconnect-cli']

def digest(data):return hashlib.sha256(data).hexdigest()
def save(path,value):
 path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(value,indent=2)+'\n');path.chmod(0o600)
def require_user():
 if hasattr(os,'geteuid') and os.geteuid()==0:raise ValueError('Run setup as the desktop user, without sudo.')
def doctor():
 try:release=platform.freedesktop_os_release()
 except OSError:release={}
 immutable=any(Path(x).exists() for x in ['/run/ostree-booted','/etc/NIXOS'])
 manager=next((x for x in ['apt-get','dnf','pacman','zypper','nix','rpm-ostree'] if shutil.which(x)),None)
 return {'platform':sys.platform,'distribution':release.get('ID','unknown'),'version':release.get('VERSION_ID','unknown'),
  'family':release.get('ID_LIKE',''),'architecture':platform.machine(),'package_manager':manager,
  'native_declarative_workflow_required':immutable,'session_type':os.environ.get('XDG_SESSION_TYPE','unknown'),
  'wayland_available':bool(os.environ.get('WAYLAND_DISPLAY')),'commands':{x:bool(shutil.which(x)) for x in COMMANDS},
  'free_disk_gib':round(shutil.disk_usage(Path.home()).free/(1024**3),1),
  'status':'inspection only; package availability and API compatibility must be verified on target'}
def bundle():
 archive=ROOT/'reference-source.tar.gz';manifest=json.loads((ROOT/'SOURCE_MANIFEST.json').read_text())
 if digest(archive.read_bytes())!=manifest['archive_sha256']:raise ValueError('Source bundle checksum mismatch')
 return archive,manifest

def extract():
 require_user();archive,manifest=bundle();STATE.mkdir(mode=0o700,exist_ok=True)
 source=STATE/'source'
 with tempfile.TemporaryDirectory(dir=STATE,prefix='.source-') as folder:
  target=Path(folder)
  with tarfile.open(archive,'r:gz') as tar:
   members=tar.getmembers()
   if len(members)>2000 or sum(x.size for x in members)>20*1024*1024:raise ValueError('Oversized source archive')
   names=set()
   for entry in members:
    path=Path(entry.name)
    if path.is_absolute() or '..' in path.parts or entry.issym() or entry.islnk() or not entry.isfile():raise ValueError('Unsafe archive member')
    if entry.name in names:raise ValueError('Duplicate archive member')
    names.add(entry.name)
    expected=manifest['files'].get(entry.name)
    data=tar.extractfile(entry).read()
    if not expected or digest(data)!=expected['sha256']:raise ValueError('Source file hash mismatch: '+entry.name)
    output=target/path;output.parent.mkdir(parents=True,exist_ok=True);output.write_bytes(data)
   if names!=set(manifest['files']):raise ValueError('Source manifest differs from archive')
  if source.exists():
   existing={str(p.relative_to(source)):digest(p.read_bytes()) for p in source.rglob('*') if p.is_file()}
   if existing!={k:v['sha256'] for k,v in manifest['files'].items()}:raise ValueError('Extracted source contains edits or an older version; preserve/rename .setup-state/source before extracting again.')
  else:shutil.copytree(target,source)
 return source

def personalize(text,name):
 """Change user-facing Python string literals while preserving internal IDs/paths/classes."""
 display=name or 'Assistant';wake=display.lower()
 def replace(value):
  value=re.sub(r'(?<![\w./-])Friday(?![\w.-])',display,value)
  # Bare executable/file names remain internal. Wake phrases and regex alternatives change.
  if value!='friday':value=re.sub(r'(?<![\w./-])friday(?![\w.-])',wake,value)
  return value
 tokens=[]
 for token in tokenize.generate_tokens(io.StringIO(text).readline):
  if token.type==tokenize.STRING:
   try:value=ast.literal_eval(token.string)
   except (ValueError,SyntaxError):value=None
   if isinstance(value,str):token=token._replace(string=repr(replace(value)))
  tokens.append(token)
 return tokenize.untokenize(tokens)

def configure(name,disabled):
 require_user()
 if disabled:name=None
 elif not name:name=input('Assistant name (short word, or none): ').strip()
 if name and name.lower()=='none':name=None
 if name and not re.fullmatch(r'[A-Za-z][A-Za-z0-9]{0,23}',name):raise ValueError('Use one short name with letters/digits, starting with a letter.')
 config={'assistant_enabled':bool(name),'assistant_name':name,'wake_listening_enabled':False,'language':'en','web_search_enabled':False}
 save(STATE/'preferences.json',config);return config

def stage():
 require_user();source=extract()
 if not (STATE/'preferences.json').exists():raise ValueError('Run configure first; assistant naming is never silently forced.')
 pref=json.loads((STATE/'preferences.json').read_text());home=str(Path.home());name=pref.get('assistant_name')
 rendered=STATE/'staged';rendered.mkdir(mode=0o700,exist_ok=True)
 # Preserve earlier rendered/adapted source before regenerating; live configuration is never touched.
 if any(rendered.iterdir()):
  import time
  history=STATE/'staged-history'/str(time.time_ns());history.parent.mkdir(parents=True,exist_ok=True);shutil.copytree(rendered,history)
 for child in list(rendered.iterdir()):
  if child.is_dir():shutil.rmtree(child)
  else:child.unlink()
 files=[]
 for file in sorted((source/'templates').rglob('*')):
  if not file.is_file():continue
  relative=file.relative_to(source/'templates')
  if not pref['assistant_enabled'] and ('friday' in relative.parts or file.name.startswith('friday')):continue
  output=rendered/str(relative).removesuffix('.in');output.parent.mkdir(parents=True,exist_ok=True)
  text=file.read_text().replace('{{HOME}}',home)
  if output.suffix=='.py':text=personalize(text,name)
  if '{{HOME}}' in text:raise ValueError('Unresolved home placeholder')
  output.write_text(text)
  if output.suffix=='.py':ast.parse(text,filename=str(relative))
  files.append({'path':str(output.relative_to(rendered)),'sha256':digest(output.read_bytes())})
 shutil.copytree(source/'profiles',rendered/'profiles',dirs_exist_ok=True)
 if pref['assistant_enabled']:
  assistant_config=rendered/'config/friday';assistant_config.mkdir(parents=True,exist_ok=True)
  (assistant_config/'wake-paused').touch(mode=0o600)
  save(assistant_config/'preferences.json',pref)
 files=[{'path':str(p.relative_to(rendered)),'sha256':digest(p.read_bytes())} for p in sorted(rendered.rglob('*')) if p.is_file()]
 save(STATE/'stage-manifest.json',{'preferences':pref,'files':files,'applied_to_live_system':False})
 return {'source':str(source),'staged':str(rendered),'files':len(files),'next':'AI: inspect docs/module-map.md, resolve dependencies, checkpoint exact destinations, install and verify modules.'}

def check():
 source=extract();count=0
 for file in source.rglob('*'):
  if not file.is_file():continue
  if file.name.endswith(('.py','.py.in')) or (file.suffix=='.in' and file.read_text().startswith(('#!/usr/bin/python','#!/usr/bin/env python'))):
   ast.parse(file.read_text().replace('{{HOME}}','/home/example'),filename=str(file.relative_to(source)));count+=1
 return {'bundle_integrity':'passed','python_sources_parsed':count,'note':'Static integrity/syntax checks; this does not certify target hardware or live desktop behavior.'}

def allowed(path):
 path=Path(path).expanduser();home=Path.home().resolve();resolved=path.resolve()
 scopes=['.config/niri','.config/noctalia','.config/quickshell','.config/systemd/user','.local/bin','.local/share/mac-control-center','.local/share/mac-spotlight','.local/share/mac-capture','.local/share/mac-desktop-design','.local/share/friday','.local/share/noctalia/plugins','.local/share/backgrounds/niri-mac','.local/state/mac-appearance']
 if not any(resolved.is_relative_to(home/x) for x in scopes):raise ValueError('Checkpoint destination outside approved desktop scopes')
 if path.is_symlink() or (path.exists() and not path.is_file()):raise ValueError('Checkpoint only explicit regular files, not symlinks/directories')
 return path.absolute()

def checkpoint(paths):
 require_user();import time
 root=STATE/'checkpoints'/str(time.time_ns());root.mkdir(parents=True,mode=0o700);entries=[]
 for index,item in enumerate(paths):
  target=allowed(item);entry={'path':str(target),'existed':target.exists()}
  if target.exists():
   backup=root/str(index);shutil.copy2(target,backup);entry.update(backup=str(index),before_sha256=digest(backup.read_bytes()),mode=target.stat().st_mode&0o777)
  entries.append(entry)
 save(root/'manifest.json',{'files':entries,'sealed':False});return {'checkpoint':root.name}

def modify_checkpoint(ident,restore=False):
 require_user()
 if not ident.isdigit():raise ValueError('Invalid checkpoint ID')
 root=STATE/'checkpoints'/ident;manifest=json.loads((root/'manifest.json').read_text())
 if not restore:
  for entry in manifest['files']:
   target=allowed(entry['path']);entry['applied_sha256']=digest(target.read_bytes()) if target.exists() else None
  manifest['sealed']=True;save(root/'manifest.json',manifest);return {'sealed':ident}
 if not manifest.get('sealed'):raise ValueError('Seal after deployment before using guarded restore.')
 for entry in manifest['files']:
  target=allowed(entry['path']);current=digest(target.read_bytes()) if target.exists() else None
  if current!=entry['applied_sha256']:raise ValueError('User edits detected; manual merge required: '+str(target))
 for entry in manifest['files']:
  target=allowed(entry['path'])
  if entry['existed']:
   backup=root/entry['backup']
   if digest(backup.read_bytes())!=entry['before_sha256']:raise ValueError('Backup checksum mismatch')
 for entry in manifest['files']:
  target=allowed(entry['path'])
  if entry['existed']:
   target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(root/entry['backup'],target);target.chmod(entry['mode'])
  else:target.unlink(missing_ok=True)
 return {'restored':ident,'next':'Validate/reload the affected configuration and restore prior service enablement from the implementation report.'}

def main():
 parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='command',required=True)
 sub.add_parser('doctor');sub.add_parser('extract');sub.add_parser('stage');sub.add_parser('check')
 conf=sub.add_parser('configure');group=conf.add_mutually_exclusive_group();group.add_argument('--assistant-name');group.add_argument('--no-assistant',action='store_true')
 cp=sub.add_parser('checkpoint');cp.add_argument('paths',nargs='+')
 for verb in ['seal','restore']:sub.add_parser(verb).add_argument('checkpoint')
 args=parser.parse_args()
 if args.command=='doctor':value=doctor()
 elif args.command=='configure':value=configure(args.assistant_name,args.no_assistant)
 elif args.command=='extract':value={'source':str(extract())}
 elif args.command=='stage':value=stage()
 elif args.command=='check':value=check()
 elif args.command=='checkpoint':value=checkpoint(args.paths)
 else:value=modify_checkpoint(args.checkpoint,args.command=='restore')
 print(json.dumps(value,indent=2))
if __name__=='__main__':
 try:main()
 except (OSError,ValueError,KeyError,tarfile.TarError) as error:raise SystemExit(str(error))
