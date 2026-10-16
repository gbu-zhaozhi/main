# -*- coding: utf-8 -*-
"""Create team-showcase block override with subpath-safe URLs.

Copies the theme's blox/team-showcase/block.html into the project's
layouts/_partials/hbx/blocks/team-showcase/ and patches:
  1. author card links:  printf "/authors/%s/"  ->  home-prefixed
  2. CTA link relLangURL fallback -> prefix root-absolute URLs with the
     home RelPermalink (Hugo's relLangURL leaves "/x/" unchanged, which
     404s under the /main/ subpath on GitHub Pages).
"""
import io, os, shutil

THEME = (r'C:/Users/zhizh/go/pkg/mod/github.com/!hugo!blox/kit/modules/'
         r'blox@v0.0.0-20260527025321-61f41d3667f1/blox/team-showcase/block.html')
DEST_DIR = r'D:/LabWebsite/main/layouts/_partials/hbx/blocks/team-showcase'
DEST = os.path.join(DEST_DIR, 'block.html')

os.makedirs(DEST_DIR, exist_ok=True)
s = io.open(THEME, encoding='utf-8').read()

header = ('{{/* Zhao Lab override of the Hugo Blox team-showcase block.\n'
          '   Only change vs upstream: internal root-absolute URLs are\n'
          '   prefixed with the site home RelPermalink so they work under\n'
          '   the GitHub Pages subpath (/main/). */}}\n')
s = header + s

# 1) author profile links (2 occurrences)
old_link = '{{ $link := printf "/authors/%s/" $profile.slug }}'
new_link = ('{{ $link := printf "%s/authors/%s/" '
            '(strings.TrimRight site.Home.RelPermalink "/") $profile.slug }}')
assert s.count(old_link) == 2, 'author link pattern count: %d' % s.count(old_link)
s = s.replace(old_link, new_link)

# 2) CTA link
old_cta = '          {{ $cta_link = $cta_link | relLangURL }}'
new_cta = ('          {{ if hasPrefix $cta_link "/" }}'
           '{{ $cta_link = printf "%s%s" (strings.TrimRight site.Home.RelPermalink "/") $cta_link }}'
           '{{ else }}'
           '{{ $cta_link = $cta_link | relLangURL }}'
           '{{ end }}')
assert old_cta in s, 'cta pattern not found'
s = s.replace(old_cta, new_cta)

io.open(DEST, 'w', encoding='utf-8', newline='\n').write(s)
print('team-showcase override written:', DEST)
