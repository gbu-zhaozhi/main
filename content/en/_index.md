---
title: ''
summary: 'Zhao Lab at Great Bay University — design and optimization of intelligent materials and structures.'
date: 2026-10-14
type: landing

sections:
  - block: lab-hero
    id: hero
    content:
      eyebrow: 'At Great Bay University · School of Advanced Engineering'
      title: '[Zhao Lab]'
      motto: 'Designing Matter, Enabling Intelligence.'
      text: 'We develop inverse design frameworks for mechanics and multiphysics problems, connecting theory, computation, additive manufacturing, and experimental validation — toward intelligent materials and structures.'
      primary_action:
        text: 'Explore our research'
        url: '/en/research/'
        style: 'solid'
      secondary_action:
        text: 'Join the lab'
        url: '/en/openings/'
        style: 'outline'
      media:
        type: 'image'
        src: 'research/hero-banner.jpg'
        alt: 'Zhao Lab research banner: inverse design, multiphysics, and intelligent materials'
    design:
      layout: 'banner'
      size: 'default'
      alignment: 'center'

  - block: markdown
    id: welcome
    content:
      title: 'Welcome to Zhao Lab'
      text: |-
        Zhao Lab is a research group in the **School of Advanced Engineering at Great Bay University**, led by **Assistant Professor Zhi Zhao**.

        Our research centers on the **design and optimization of intelligent materials and structures**. We build inverse design frameworks that co-design geometry, material distribution, and external stimuli so that a structure delivers a targeted mechanical or multifunctional response — rather than only analysing a shape that has already been chosen.

        We work across the full chain: **theoretical modelling → optimization algorithms → additive manufacturing → mechanical testing and experimental validation**. This “design–fabricate–validate” loop lets us take a computational design all the way to a physically realized structure and check it against measurement.

        Our scientific identity is rooted in **mechanics and computational design**, and extends into advanced materials, coupled multiphysics, and physically intelligent structures.

        <p class="hb-sp-intro">You can also find us on social media — scan the QR codes to follow the lab on <strong>RED (Xiaohongshu)</strong> and <strong>Douyin</strong>, or reach us via Google Scholar, e-mail, or ResearchGate.</p>
        <div class="hb-sp-links">
          <a class="hb-sp-link" href="https://scholar.google.com/citations?user=97AQtN4AAAAJ&hl=en" target="_blank" rel="noopener noreferrer"><span class="hb-sp-icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M5.242 13.769 0 9.5 12 0l12 9.5-5.242 4.269C17.548 11.249 14.978 9.5 12 9.5c-2.977 0-5.548 1.748-6.758 4.269zM12 10a7 7 0 1 0 0 14 7 7 0 0 0 0-14z"/></svg></span><span class="hb-sp-label">Google Scholar</span></a>
          <a class="hb-sp-link" href="mailto:zhaoz@gbu.edu.cn"><span class="hb-sp-icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/></svg></span><span class="hb-sp-label">E-mail</span></a>
          <a class="hb-sp-link" href="https://www.researchgate.net/profile/Zhi-Zhao-10" target="_blank" rel="noopener noreferrer"><span class="hb-sp-icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><text x="12" y="17" text-anchor="middle" font-size="11.5" font-weight="700" font-family="Georgia,serif" fill="currentColor">RG</text></svg></span><span class="hb-sp-label">ResearchGate</span></a>
        </div>
        <div class="hb-sp-qrs">
          <figure class="hb-sp-qr"><img src="/uploads/qr-xiaohongshu.png" alt="Xiaohongshu (RED) QR code" loading="lazy"><figcaption>RED</figcaption></figure>
          <figure class="hb-sp-qr"><img src="/uploads/qr-douyin.png" alt="Douyin QR code" loading="lazy"><figcaption>Douyin</figcaption></figure>
        </div>

  - block: focus-areas
    id: research
    content:
      title: 'Research Areas'
      subtitle: 'Three interconnected directions'
      text: 'Each direction has a dedicated page with an overview, representative approaches, and related publications.'
      items:
        - name: 'Architected Materials and Metamaterials'
          description: 'Materials and structures with programmable nonlinear responses, multistability, buckling, and tunable mechanical properties.'
          image: 'research/area-b.jpg'
          url: '/en/research/architected-materials/'
          cta_text: 'Learn more'
          topics:
            - Metamaterials
            - Multistability
            - Buckling
            - Programmable response
        - name: 'Multifunctional Materials and Structures'
          description: 'Magneto-mechanical and magneto-electro-mechanical coupling, programmable actuation, sensing, and multifunctional mechanical systems.'
          image: 'research/area-c.jpg'
          url: '/en/research/multifunctional-materials/'
          cta_text: 'Learn more'
          topics:
            - Magneto-mechanics
            - Mechano-electric coupling
            - Actuation
            - Sensing
        - name: 'Physical Intelligence and Advanced Applications'
          description: 'Intelligent structures, soft robotic systems, and biomedical devices that combine mechanical adaptability, actuation, and sensing.'
          image: 'research/area-d.jpg'
          url: '/en/research/physical-intelligence/'
          cta_text: 'Learn more'
          topics:
            - Intelligent structures
            - Soft robotics
            - Biomedical devices
    design:
      layout: 'cards'

  - block: content-collection
    id: publications
    content:
      title: 'Featured Publications'
      text: 'Selected papers from the group. See the [Publications](/en/publications/) page for the complete list.'
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
      title: 'People'
      subtitle: 'Principal Investigator'
      text: 'Zhao Lab is led by Assistant Professor Zhi Zhao. Postdoctoral, PhD, Master’s and undergraduate researchers will join as the group grows — see [Openings](/en/openings/).'
      user_groups:
        - name: 'Principal Investigator'
      sort_by: 'weight'
      sort_ascending: true
      cta:
        text: 'Meet the team'
        url: '/en/people/'
    design:
      max_columns: 3

  - block: markdown
    id: openings
    content:
      title: 'Openings'
      text: |-
        We welcome motivated students and researchers with backgrounds in **mechanics, mechanical engineering, civil engineering, robotics, applied physics, computer science, and aerospace engineering**.

        Members receive end-to-end research training across the full chain — theoretical modelling, optimization algorithms, scientific programming, advanced manufacturing and 3D printing, and mechanical testing with experimental validation.

        Interested applicants are invited to contact **zhaoz@gbu.edu.cn** with a CV and a short statement of research interests.

        [Read the full call →](/en/openings/)
---
