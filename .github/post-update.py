import json, os, sys
# usage: post_update.py VERSION NOTES_FILE OUT_JSON  -> Discord payload: @everyone, the Darkorado icon, what changed
v, notes, out = sys.argv[1], sys.argv[2], sys.argv[3]
items = [l.strip()[2:] for l in open(notes, encoding='utf-8').read().splitlines() if l.strip().startswith('- ')]
desc = '\n'.join('• ' + i for i in items) or 'Fixes and improvements.'
icon = os.path.exists('.github/darkorado-icon.png')
emb = {"color": 0xA855F7, "title": f"Darkorado {v} is out", "description": desc,
       "footer": {"text": "Updates install by themselves: just restart Darkorado."}}
if icon: emb["thumbnail"] = {"url": "attachment://darkorado.png"}
payload = {"username": "Darkorado", "content": "@everyone", "allowed_mentions": {"parse": ["everyone"]}, "embeds": [emb]}
if icon: payload["attachments"] = [{"id": 0, "filename": "darkorado.png"}]
open(out, 'w').write(json.dumps(payload))
