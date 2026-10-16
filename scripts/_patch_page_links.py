# -*- coding: utf-8 -*-
"""Patch page_links.html: subpath-safe root-absolute attachment URLs."""
import io

p = r'D:/LabWebsite/main/layouts/_partials/page_links.html'
s = io.open(p, encoding='utf-8').read()

old = (
    '      {{ with ($page.Resources.GetMatch $url) }}\n'
    '        {{ $url = .RelPermalink }}\n'
    '      {{ else }}\n'
    '        {{ $url = $url | relURL }}\n'
    '      {{ end }}'
)
new = (
    '      {{ with ($page.Resources.GetMatch $url) }}\n'
    '        {{ $url = .RelPermalink }}\n'
    '      {{ else }}\n'
    '        {{/* Zhao Lab patch: relURL leaves root-absolute URLs unchanged;\n'
    '             the site lives under a subpath (/main/) on GitHub Pages, so\n'
    '             prepend the home RelPermalink for root-absolute URLs. */}}\n'
    '        {{ if strings.HasPrefix $url "/" }}\n'
    '          {{ $url = printf "%s%s" (strings.TrimRight site.Home.RelPermalink "/") $url }}\n'
    '        {{ else }}\n'
    '          {{ $url = $url | relURL }}\n'
    '        {{ end }}\n'
    '      {{ end }}'
)
assert old in s, 'pattern not found in page_links.html'
s = s.replace(old, new, 1)
io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('page_links.html patched OK')
