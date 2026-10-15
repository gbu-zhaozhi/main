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
        url: '/research/'
        style: 'solid'
      secondary_action:
        text: 'Join the lab'
        url: '/openings/'
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
          url: '/research/architected-materials/'
          cta_text: 'Learn more'
          topics:
            - Metamaterials
            - Multistability
            - Buckling
            - Programmable response
        - name: 'Multifunctional Materials and Structures'
          description: 'Magneto-mechanical and magneto-electro-mechanical coupling, programmable actuation, sensing, and multifunctional mechanical systems.'
          image: 'research/area-c.jpg'
          url: '/research/multifunctional-materials/'
          cta_text: 'Learn more'
          topics:
            - Magneto-mechanics
            - Mechano-electric coupling
            - Actuation
            - Sensing
        - name: 'Physical Intelligence and Advanced Applications'
          description: 'Intelligent structures, soft robotic systems, and biomedical devices that combine mechanical adaptability, actuation, and sensing.'
          image: 'research/area-d.jpg'
          url: '/research/physical-intelligence/'
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
      text: 'Selected papers from the group. See the [Publications](/publications/) page for the complete list.'
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
      text: 'Zhao Lab is led by Assistant Professor Zhi Zhao. Postdoctoral, PhD, Master’s and undergraduate researchers will join as the group grows — see [Openings](/openings/).'
      user_groups:
        - name: 'Principal Investigator'
      sort_by: 'weight'
      sort_ascending: true
      cta:
        text: 'Meet the team'
        url: '/people/'
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

        [Read the full call →](/openings/)
---
