#!/usr/bin/env python3
"""Check the docs: every nav entry has a file, no orphan pages, internal links
resolve, frontmatter present, no stale terms, no HTML comments.
Usage: python3 scripts/check-docs.py   (exit 1 on problems)"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(ROOT)
d = json.load(open('docs.json')); nav = []
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'pages':
                for p in v: nav.append(p) if isinstance(p, str) else walk(p)
            else: walk(v)
    elif isinstance(o, list):
        for x in o: walk(x)
walk(d['navigation'])
errors = [f'NAV → missing file: {p}.mdx' for p in nav if not os.path.exists(p + '.mdx')]
mdx = []
for dp, dn, fn in os.walk('.'):
    dn[:] = [x for x in dn if x not in ('.git', 'node_modules')]
    mdx += [os.path.normpath(os.path.join(dp, f))[:-4] for f in fn if f.endswith('.mdx')]
errors += [f'ORPHAN (not in nav): {o}.mdx' for o in sorted(set(mdx) - set(nav))]
link_re = re.compile(r'(?:href=|\]\()"?(/[^"\s)#]+)(#[^"\s)]+)?')
stale = re.compile(r'(?<!first )\bAI agent\b|/automation/ai-agent\b|EzyText|Settings → Tags|Settings → SMS Templates|Settings → Templates')
for p in mdx:
    s = open(p + '.mdx').read()
    if not s.startswith('---\n'): errors.append(f'FRONTMATTER missing: {p}.mdx'); continue
    fm = s.split('---\n')[1]
    for key in ('title:', 'description:'):
        if key not in fm: errors.append(f'FRONTMATTER {key} missing: {p}.mdx')
    live = re.sub(r'\{/\*.*?\*/\}', '', s, flags=re.S)
    for m in link_re.finditer(live):
        t, anchor = m.group(1), m.group(2)
        if t.startswith(('/images/', '/videos/', '/logo/', '/favicon')): continue
        if not os.path.exists(t.lstrip('/') + '.mdx'): errors.append(f'LINK {p}.mdx → {t} (no such page)'); continue
        if anchor:
            target = open(t.lstrip('/') + '.mdx').read()
            ids = [re.sub(r'[^a-z0-9]+', '-', h.lower()).strip('-') for h in re.findall(r'^#{1,6} (.+)$', target, re.M)]
            if anchor[1:] not in ids: errors.append(f'ANCHOR {p}.mdx → {t}{anchor} (no such heading)')
    for m in stale.finditer(live): errors.append(f'STALE {p}.mdx: "{m.group(0)}"')
    if '<!--' in live: errors.append(f'HTML COMMENT (breaks MDX) in {p}.mdx')
print(f'{len(nav)} nav pages, {len(mdx)} mdx files, {len(errors)} problem(s)')
for e in errors: print(e)
sys.exit(1 if errors else 0)
