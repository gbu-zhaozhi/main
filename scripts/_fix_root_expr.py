# -*- coding: utf-8 -*-
"""Switch the subpath root from site.Home.RelPermalink (language-specific!)
to the baseURL path (language-independent).

site.Home.RelPermalink on EN pages = /main/en/ which:
  - doubled the /en/ prefix for links already carrying it (/main/en/en/...)
  - wrongly prefixed shared assets (/main/en/uploads/...)
The baseURL path (/main) is correct in all cases: content links keep their
own /en/ language prefix, and shared /uploads/... paths get /main only.
"""
import io

# old root expressions -> new root expression
OLD_HOME = '{{ $home := strings.TrimRight "/" site.Home.RelPermalink }}'
NEW_HOME = '{{ $home := strings.TrimRight "/" ((urls.Parse site.BaseURL).Path) }}'

OLD_INLINE = 'strings.TrimRight "/" site.Home.RelPermalink'
NEW_INLINE = 'strings.TrimRight "/" ((urls.Parse site.BaseURL).Path)'

files = [
    r'D:/LabWebsite/main/layouts/_partials/hbx/blocks/lab-hero/block.html',
    r'D:/LabWebsite/main/layouts/_partials/hbx/blocks/focus-areas/block.html',
    r'D:/LabWebsite/main/layouts/_partials/page_links.html',
    r'D:/LabWebsite/main/layouts/_partials/hbx/blocks/team-showcase/block.html',
    r'D:/LabWebsite/main/layouts/_markup/render-link.html',
]

for path in files:
    s = io.open(path, encoding='utf-8').read()
    n = 0
    if OLD_HOME in s:
        n += s.count(OLD_HOME)
        s = s.replace(OLD_HOME, NEW_HOME)
    if OLD_INLINE in s:
        n += s.count(OLD_INLINE)
        s = s.replace(OLD_INLINE, NEW_INLINE)
    assert n > 0, 'nothing replaced in ' + path
    assert 'site.Home.RelPermalink' not in s, 'leftover in ' + path
    io.open(path, 'w', encoding='utf-8', newline='\n').write(s)
    print('%s: %d replaced' % (path.split('/')[-2] + '/' + path.split('/')[-1], n))

print('DONE')
