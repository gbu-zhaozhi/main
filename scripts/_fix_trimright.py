# -*- coding: utf-8 -*-
"""Fix reversed strings.TrimRight argument order in all subpath patches +
remove debug markers from lab-hero.

Hugo 0.168 signature: strings.TrimRight CUTSET STRING
Our patches had it as (STRING, CUTSET), which trimmed the URL to "".
"""
import io, re

WRONG = 'strings.TrimRight site.Home.RelPermalink "/"'
RIGHT = 'strings.TrimRight "/" site.Home.RelPermalink'

# ---- 1. lab-hero: strip debug fragments first, then fix TrimRight -------
hero = r'D:/LabWebsite/main/layouts/_partials/hbx/blocks/lab-hero/block.html'
s = io.open(hero, encoding='utf-8').read()

# line 87: remove everything after the first }} up to line end (QQ debug)
lines = s.split('\n')
for idx, ln in enumerate(lines):
    if ln.startswith('{{ $home := '):
        lines[idx] = ln.split('}}', 1)[0] + '}}'
    elif '"HOME=["' in ln or 'HOME=[' in ln:
        # remove the debug actions appended after $sa_href line
        cut = ln.find('{{ "HOME=[" }}')
        lines[idx] = ln[:cut].rstrip()
    elif 'ZZA' in ln:
        cut = ln.find('{{ site.Home.RelPermalink }}ZZA')
        lines[idx] = ln[:cut].rstrip()
s = '\n'.join(lines)
assert 'QQ' not in s and 'ZZA' not in s and 'HOME=[' not in s, 'debug leftovers'
assert WRONG in s
s = s.replace(WRONG, RIGHT)
io.open(hero, 'w', encoding='utf-8', newline='\n').write(s)
print('lab-hero: debug removed + TrimRight fixed')

# ---- 2..5: fix TrimRight in the other patched files ---------------------
for path in [
    r'D:/LabWebsite/main/layouts/_partials/hbx/blocks/focus-areas/block.html',
    r'D:/LabWebsite/main/layouts/_partials/page_links.html',
    r'D:/LabWebsite/main/layouts/_partials/hbx/blocks/team-showcase/block.html',
    r'D:/LabWebsite/main/layouts/_markup/render-link.html',
]:
    t = io.open(path, encoding='utf-8').read()
    n = t.count(WRONG)
    assert n > 0, 'no TrimRight found in ' + path
    t = t.replace(WRONG, RIGHT)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(t)
    print('%s: %d occurrence(s) fixed' % (path.split('/')[-1], n))

print('ALL PATCHED')
