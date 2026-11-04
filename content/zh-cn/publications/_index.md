---
title: '论文发表'
summary: 'Zhao Lab 同行评审期刊论文，按发表时间由新到旧排列。'
date: 2026-10-14
type: landing

sections:
  - block: journal-strip
    id: journals
    content:
      title: '论文发表'

  - block: content-collection
    id: publications-list
    content:
      count: 100
      filters:
        folders:
          - publications
      sort_by: 'Date'
      sort_ascending: false
    design:
      view: citation

  - block: markdown
    id: publications-note
    content:
      title: '说明'
      text: |-
        作者顺序与共同贡献标注均以原始记录为准。† 表示共同第一作者（同等贡献），\* 表示通讯作者。

        *本列表由人工维护。预印本与会议论文将在发表后陆续补充。*
---
