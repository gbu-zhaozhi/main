# -*- coding: utf-8 -*-
"""Comprehensive URL audit for the /main/ subpath deployment.

Every root-relative href/src must:
  - start with /main/
  - resolve to an existing file in public/ (URL-decoded, index.html for dirs)
Excludes: alias redirect stubs, and verifies key spot checks.
"""
import re, pathlib, urllib.parse

pub = pathlib.Path(r'D:/LabWebsite/main/public')

zh = (pub/'index.html').read_text(encoding='utf-8')
en = (pub/'en/index.html').read_text(encoding='utf-8')
print('== spot checks ==')
print('ZH hero  :', re.findall(r'href=[\"\']?([^\"\'> ]*)[\"\']?[^>]*>了解研究方向', zh))
print('EN hero  :', re.findall(r'href=[\"\']?([^\"\'> ]*)[\"\']?[^>]*>Explore our research', en))
print('ZH QR    :', re.findall(r'src=[\"\']?([^\"\'> ]*qr-[^\"\'> ]*)', zh))
print('EN QR    :', re.findall(r'src=[\"\']?([^\"\'> ]*qr-[^\"\'> ]*)', en))
print('EN focus :', sorted(set(re.findall(r'href=[\"\']?(/main/en/research/[^\"\'> ]*)', en)))[:4])
print('EN people cta:', '/main/en/people/' in en or '/main/people/' in en)
pubp = (pub/'en/publications/additive-manufacturing-2025/index.html').read_text(encoding='utf-8')
print('EN pub PDF:', re.findall(r'href=[\"\']?([^\"\'> ]*additive-manufacturing-2025.pdf)', pubp))
edu = (pub/'en/education/index.html').read_text(encoding='utf-8')
print('EN edu links:', re.findall(r'href=[\"\']?([^\"\'> ]*smo-2021-review[^\"\'> ]*)', edu))
con = (pub/'en/contact/index.html').read_text(encoding='utf-8')
print('EN contact openings link:', re.findall(r'href=[\"\']?([^\"\'> ]*openings[^\"\'> ]*)', con)[:2])

print()
print('== full crawl ==')
missing = {}
count = 0
skipped_stubs = 0
for fp in pub.rglob('*.html'):
    s = fp.read_text(encoding='utf-8', errors='ignore')
    if 'refresh' in s and len(s) < 800:
        skipped_stubs += 1
        continue
    for url in re.findall(r'(?:href|src)=[\"\']?(/[a-zA-Z0-9][^\"\'> ]*)', s):
        count += 1
        if not url.startswith('/main/'):
            missing.setdefault('NO-PREFIX ' + url, []).append(str(fp.relative_to(pub)))
            continue
        # strip query/fragment, URL-decode
        target = url.split('#')[0].split('?')[0]
        target = urllib.parse.unquote(target).rstrip('/')
        t = pub / target[len('/main/'):]
        if t.is_dir():
            t = t / 'index.html'
        elif not t.suffix:
            t = pub / (target[len('/main/'):] + '.html')
        if not t.exists():
            missing.setdefault('BROKEN ' + url, []).append(str(fp.relative_to(pub)))

print('root-relative URLs:', count, '| alias stubs skipped:', skipped_stubs,
      '| problems:', len(missing))
for k, v in sorted(missing.items())[:15]:
    print('  ', k, '<-', v[0])
