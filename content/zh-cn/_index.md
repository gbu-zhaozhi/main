---
title: ''
summary: 'Zhao Lab——大湾区大学，智能材料与结构的设计优化。'
date: 2026-10-14
type: landing

sections:
  - block: lab-hero
    id: hero
    content:
      eyebrow: '大湾区大学 · 先进工程学院'
      title: '[Zhao Lab]'
      motto: 'Designing Matter, Enabling Intelligence.'
      motto_sub: '设计物质，赋予智能'
      text: '**智能材料与结构的设计优化。** 我们发展面向力学及多物理场问题的逆向设计框架，将理论计算、增材制造制备与实验表征紧密结合。'
      primary_action:
        text: '了解研究方向'
        url: '/research/'
        style: 'solid'
      secondary_action:
        text: '加入课题组'
        url: '/openings/'
        style: 'outline'
      media:
        type: 'image'
        src: 'research/hero-banner.jpg'
        alt: 'Zhao Lab 研究视觉：逆向设计、多物理场与智能材料'
    design:
      layout: 'banner'
      size: 'default'
      alignment: 'center'

  - block: markdown
    id: welcome
    content:
      title: '欢迎来到 Zhao Lab'
      text: |-
        Zhao Lab 隶属**大湾区大学先进工程学院**，由**助理教授、研究员赵志**领衔。

        我们的研究聚焦**智能材料与结构的设计优化**，致力于发展面向力学及多物理场问题的**逆向设计框架**：同步设计几何构型、材料分布与外部激励，使结构获得预期的非线性力学响应或多功能响应，而不是仅对既定构型进行分析。

        课题组坚持 **“设计—制造—实验验证”** 贯通的研究思路，研究链条覆盖**理论建模 → 优化算法 → 增材制造制备 → 力学测试与实验表征**，使计算设计能够真正落地为可制备、可测量的物理结构。

        我们的科学定位以**力学与计算设计**为根基，并延伸至先进材料、耦合多物理场与物理智能结构。

        <p class="hb-sp-intro">也欢迎在社交媒体上找到我们——扫码关注课题组的<strong>小红书</strong>与<strong>抖音</strong>账号，或通过谷歌学术、邮箱与 ResearchGate 与我们取得联系。</p>
        <div class="hb-sp-links">
          <a class="hb-sp-link" href="https://scholar.google.com/citations?user=97AQtN4AAAAJ&hl=en" target="_blank" rel="noopener noreferrer"><span class="hb-sp-icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M5.242 13.769 0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z"/></svg></span><span class="hb-sp-label">谷歌学术</span></a>
          <a class="hb-sp-link" href="mailto:zhaoz@gbu.edu.cn"><span class="hb-sp-icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/></svg></span><span class="hb-sp-label">邮箱</span></a>
          <a class="hb-sp-link" href="https://www.researchgate.net/profile/Zhi-Zhao-10" target="_blank" rel="noopener noreferrer"><span class="hb-sp-icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><text x="12" y="17" text-anchor="middle" font-size="11.5" font-weight="700" font-family="Georgia,serif" fill="currentColor">RG</text></svg></span><span class="hb-sp-label">ResearchGate</span></a>
        </div>
        <!-- QR 图用相对路径：站点部署在 GitHub Pages 子路径 /main/ 下时，
             绝对路径 /uploads/... 会 404；中文首页位于站点根（/main/），
             相对路径 uploads/... 在本地根路径预览和子路径部署下均正确。 -->
        <div class="hb-sp-qrs">
          <figure class="hb-sp-qr"><img src="uploads/qr-xiaohongshu.png" alt="小红书二维码" loading="lazy"><figcaption>小红书</figcaption></figure>
          <figure class="hb-sp-qr"><img src="uploads/qr-douyin.png" alt="抖音二维码" loading="lazy"><figcaption>抖音</figcaption></figure>
        </div>

  - block: focus-areas
    id: research
    content:
      title: '研究方向'
      subtitle: '三个相互关联的研究方向'
      text: '每个方向均设有独立页面，介绍研究内涵、代表性方法与相关论文。'
      items:
        - name: '构筑材料与力学超材料'
          description: '设计具有可编程非线性响应、多稳态、屈曲与可调力学性能的材料与结构。'
          image: 'research/area-b.jpg'
          url: '/research/architected-materials/'
          cta_text: '了解更多'
          topics:
            - 力学超材料
            - 多稳态
            - 屈曲
            - 可编程响应
        - name: '多功能材料与结构'
          description: '研究磁-力耦合与磁-电-力耦合、可编程驱动、传感与多功能力学系统。'
          image: 'research/area-c.jpg'
          url: '/research/multifunctional-materials/'
          cta_text: '了解更多'
          topics:
            - 磁-力耦合
            - 力-电耦合
            - 可编程驱动
            - 传感
        - name: '物理智能与先进应用'
          description: '探索融合力学适应性、驱动与传感的智能结构、软体机器人系统与生物医疗器件。'
          image: 'research/area-d.jpg'
          url: '/research/physical-intelligence/'
          cta_text: '了解更多'
          topics:
            - 智能结构
            - 软体机器人
            - 生物医疗器件
    design:
      layout: 'cards'

  - block: content-collection
    id: publications
    content:
      title: '代表性论文'
      text: '课题组精选论文。完整列表请见[论文发表](/publications/)页面。'
      count: 4
      filters:
        folders:
          - publications
        featured_only: true
      sort_by: 'Date'
      sort_ascending: false
    design:
      view: citation

  - block: team-showcase
    id: people
    content:
      title: '团队成员'
      subtitle: '课题负责人'
      text: 'Zhao Lab 由助理教授、研究员赵志领衔。随着课题组发展，将陆续吸纳博士后、博士研究生、硕士研究生与本科生科研助理——详见[招生招聘](/openings/)。'
      user_groups:
        - name: 'Principal Investigator'
      sort_by: 'weight'
      sort_ascending: true
      cta:
        text: '查看团队成员'
        url: '/people/'
    design:
      max_columns: 3

  - block: markdown
    id: openings
    content:
      title: '招生招聘'
      text: |-
        课题组长期招收**力学、机械、土木、机器人、应用物理、计算机、航天航空**等相关专业的研究助理、硕士研究生、博士研究生与博士后。

        课题组兼顾计算与实验，学生可完整参与从**理论建模、优化算法开发、科学编程、增材制造与 3D 打印制备到力学测试表征**的全链条科研训练。

        欢迎热爱科研、有扎实力学及编程基础、动手能力强的同学邮件联系：**zhaoz@gbu.edu.cn**。

        [查看完整招生信息 →](/openings/)
---
