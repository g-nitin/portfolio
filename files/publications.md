---
layout: page
title: Publications
---

<div class="publication-list">

  <!-- 2026 / In Press -->
  <h3 class="timeline-year">2026</h3>

  <div class="publication">
    <div class="publication-title">
      GAICo: A Deployed and Extensible Framework for Evaluating Diverse and Multimodal Generative AI Outputs
    </div>
    <div class="publication-authors">
      <b>N. Gupta</b>, P. Koppisetti, K. Lakkaraju, B. Srivastava
    </div>
    <div class="publication-venue">
      IAAI/AAAI 2026 (In-Press)
      <a href="https://arxiv.org/abs/2508.16753" class="publication-link" target="_blank" title="View ArXiv">
        <i class="fas fa-external-link-alt"></i>
      </a>
    </div>
    <div class="abstract-container">
      <input type="checkbox" id="abstract-gaico1" class="abstract-toggle">
      <label for="abstract-gaico1" class="abstract-btn">Show Abstract</label>
      <div class="publication-abstract">
        The rapid proliferation of Generative AI (GenAI) into diverse, high-stakes domains necessitates robust and reproducible evaluation methods. However, practitioners often resort to ad-hoc, non-standardized scripts, as common metrics are often unsuitable for specialized, structured outputs (e.g., automated plans, time-series) or holistic comparison across modalities (e.g., text, audio, and image). This fragmentation hinders comparability and slows AI system development. To address this challenge, we present GAICo (Generative AI Comparator): a deployed, open-source Python library that streamlines and standardizes GenAI output comparison. GAICo provides a unified, extensible framework supporting a comprehensive suite of reference-based metrics for unstructured text, specialized structured data formats, and multimedia (images, audio). Its architecture features a high-level API for rapid, end-to-end analysis, from multi-model comparison to visualization and reporting, alongside direct metric access for granular control. We demonstrate GAICo's utility through a detailed case study evaluating and debugging complex, multi-modal AI Travel Assistant pipelines. GAICo empowers AI researchers and developers to efficiently assess system performance, make evaluation reproducible, improve development velocity, and ultimately build more trustworthy AI systems, aligning with the goal of moving faster and safer in AI deployment. Since its release on PyPI in Jun 2025, the tool has been downloaded over 13K times, across versions, by Aug 2025, demonstrating growing community interest. 
      </div>
    </div>
  </div>

  <div class="publication">
    <div class="publication-title">
      GAICo: Demonstrating a Unified Framework for Multi-Modal GenAI Evaluation
    </div>
    <div class="publication-authors">
      P. Koppisetti, <b>N. Gupta</b>, K. Lakkaraju, B. Srivastava
    </div>
    <div class="publication-venue">
      AAAI Demonstration 2026 (In-Press)
    </div>
  </div>

  <div class="publication">
    <div class="publication-title">
      Promoting Nutrition Adherence with Convenience Using Group Recommendations and Multimodal Food Reasoning - Initial Results
    </div>
    <div class="publication-authors">
      <b>N. Gupta</b>, B. Srivastava, V. Nagpal, L. Valluru, K. Lakkaraju, Z. Abdulrahman, A. Davison
    </div>
    <div class="publication-venue">
      WAIN workshop at ICDM 2025 (In-press)
      <!-- <a href="https://ojs.aaai.org/index.php/ICAPS/article/view/36141" 
         class="publication-link" 
         target="_blank"
         title="View Publication">
        <i class="fas fa-external-link-alt"></i>
      </a> -->
    </div>
    <div class="abstract-container">
      <input type="checkbox" id="abstract-beacon" class="abstract-toggle">
      <label for="abstract-beacon" class="abstract-btn">Show Abstract</label>
      <div class="publication-abstract">
        A common yet regular decision made by people, whether healthy or with any health condition, is to decide what to have in meals like breakfast, lunch, and dinner, which typically consist of a combination of foods for appetizers, main courses, side dishes, desserts, and beverages. However, this decision is often seen as a trade-off between nutritious choices (e.g., salt and sugar levels, nutritional content) and convenience (e.g., cost, speed of access, cuisine type, food source type). We present a data-driven solution for meal recommendations that considers customizable meal configurations and time horizons. This solution balances user preferences while taking into account a food’s constituents and cooking process. Beyond the problem formulation, our contributions include introducing goodness measures, a recipe conversion method from text to the recently introduced multimodal rich recipe representation (R3) format,  learning methods using contextual bandits that show promising preliminary results, and the prototype, usage-inspired BEACON system. 
      </div>
    </div>
  </div>

  <!-- <div class="publication">
    <div class="publication-title">
      FABLE: A Novel Data-Flow Analysis Benchmark on Procedural Text for Large Language Model Evaluation
    </div>
    <div class="publication-authors">
      V. Pallagani, <b>N. Gupta</b>, B. Muppasani, B. Srivastava
    </div>
    <div class="publication-venue">
      Pre-Print (under review)
      <a href="https://arxiv.org/abs/2505.24258" 
         class="publication-link" 
         target="_blank"
         title="View Publication">
        <i class="fas fa-external-link-alt"></i>
      </a>
    </div>
    <div class="abstract-container">
      <input type="checkbox" id="abstract-fable" class="abstract-toggle">
      <label for="abstract-fable" class="abstract-btn">Show Abstract</label>
      <div class="publication-abstract">
        Understanding how data moves, transforms, and persists, known as data flow, is fundamental to reasoning in procedural tasks. Despite their fluency in natural and programming languages, large language models (LLMs), although increasingly being applied to decisions with procedural tasks, have not been systematically evaluated for their ability to perform data-flow reasoning. We introduce FABLE, an extensible benchmark designed to assess LLMs' understanding of data flow using structured, procedural text. FABLE adapts eight classical data-flow analyses from software engineering: reaching definitions, very busy expressions, available expressions, liv e variable analysis, interval analysis, type-state analysis, taint analysis, and concurrency analysis. These analyses are instantiated across three real-world domains: cooking recipes, travel routes, and automated plans. The benchmark includes 2,400 question-answer pairs, with 100 examples for each domain-analysis combination. We evaluate three types of LLMs: a reasoning-focused model (DeepSeek-R1 8B), a general-purpose model (LLaMA 3.1 8B), and a code-specific model (Granite Code 8B). Each model is tested using majority voting over five sampled completions per prompt. Results show that the reasoning model achieves higher accuracy, but at the cost of over 20 times slower inference compared to the other models. In contrast, the general-purpose and code-specific models perform close to random chance. FABLE provides the first diagnostic benchmark to systematically evaluate data-flow reasoning and offers insights for developing models with stronger procedural understanding. 
      </div>
    </div>
  </div> -->

  <!-- 2025 -->
  <h3 class="timeline-year">2025</h3>

  <div class="publication">
    <div class="publication-title">
      Building a Plan Ontology to Represent and Exploit Planning Knowledge and Its Applications
    </div>
    <div class="publication-authors">
      B. Muppasani, <b>N. Gupta</b>, V. Pallagani, B. Srivastava, R. Mutharaju, M. N. Huhns, and V. Narayanan
    </div>
    <div class="publication-venue">
      Discover Data Journal (Nov 2025)
      <a href="https://link.springer.com/article/10.1007/s44248-025-00093-9" 
         class="publication-link" 
         target="_blank"
         title="View Publication">
        <i class="fas fa-external-link-alt"></i>
      </a>
    </div>
    <div class="abstract-container">
      <input type="checkbox" id="abstract-onto" class="abstract-toggle">
      <label for="abstract-onto" class="abstract-btn">Show Abstract</label>
      <div class="publication-abstract">
        Ontologies are known for their ability to organize rich metadata, support the identification of novel insights via semantic queries, and promote reuse. In this paper, we consider the problem of automated planning, where the objective is to find a sequence of actions that will move an agent from an initial state of the world to a desired goal state. We hypothesize that given a large number of available planners and diverse planning domains, they carry essential information that can be leveraged to improve many ontology applications. We use open data on planning domains and planners to construct the most comprehensive planning ontology to date, based on supported competency questions, and demonstrate its applications in two practical use cases - planner selection and plan explanation. We have also made the ontology and associated resources available to the AI and data communities to promote further research.
      </div>
    </div>
  </div>

  <div class="publication">
    <div class="publication-title">
      Revisiting LLMs in Planning from Literature Review: a Semi-Automated Analysis Approach and Evolving Categories Representing Shifting Perspectives
    </div>
    <div class="publication-authors">
      V. Pallagani, <b>N. Gupta</b>, B. Muppasani, B. Srivastava
    </div>
    <div class="publication-venue">
      ICAPS 2025 (Sept 2025)
      <a href="https://ojs.aaai.org/index.php/ICAPS/article/view/36141" 
         class="publication-link" 
         target="_blank"
         title="View Publication">
        <i class="fas fa-external-link-alt"></i>
      </a>
    </div>
    <div class="abstract-container">
      <input type="checkbox" id="abstract-revisit" class="abstract-toggle">
      <label for="abstract-revisit" class="abstract-btn">Show Abstract</label>
      <div class="publication-abstract">
        Tracking the rapidly evolving literature at the intersection of large language models (LLMs) and planning has become increasingly complex due to significant growth in research output and shifting thematic focuses. Building on the survey by Pallagani et al.(2024), which organized 126 papers collected till November 2023 into eight categories, we present a platform that automates the extraction, categorization, and trend analysis of new papers. Our analysis reports on category drift, identifying evolving perspectives on the use of LLMs for planning. Our analysis reveals a decline in the percentage of papers for six categories, an increase in two, and the emergence of two new categories. Specifically, we contribute by (1) developing an automated system for categorizing new papers into existing or emergent categories,(2) reporting on category shifts with the addition of 47 new papers till September 2024, and (3) introducing a platform for continuous extraction, categorization, and trend tracking in LLM and planning research. This platform also features a leaderboard to encourage innovations in automated paper categorization.
      </div>
    </div>
  </div>

  <div class="publication">
    <div class="publication-title">
      Towards Enhancing Road Safety in South Carolina Using Insights from Traffic and Driver-Education Data (Student Abstract)
    </div>
    <div class="publication-authors">
      <b>N. Gupta</b>, B. Muppasani, S. Srivastava, A. Goel, R. Hartfield, T. Buehrig, M. Reck, E. Kennedy, K. Poore, K. Tremblay, B. Srivastava, and L. Vasconcelos 
    </div>
    <div class="publication-venue">
      AAAI 2025 Student Abstract (Apr 2025)
      <a href="https://ojs.aaai.org/index.php/AAAI/article/view/35260" 
         class="publication-link" 
         target="_blank"
         title="View Publication">
        <i class="fas fa-external-link-alt"></i>
      </a>
    </div>
    <div class="abstract-container">
      <input type="checkbox" id="abstract-student" class="abstract-toggle">
      <label for="abstract-student" class="abstract-btn">Show Abstract</label>
      <div class="publication-abstract">
        In this student paper, we report on our project to enhance road safety in South Carolina (SC) by analyzing traffic data provided by the Department of Transportation and evaluating the impact of a school-level student driver education program called Alive@25. We improve the understanding of road safety using these traffic and training data to understand collision patterns and areas for improvement and assess training coverage gaps. Our approach combines geospatial analysis, economic impact assessment, temporal trend analysis, and interactive visualizations while leveraging AI techniques to clean and analyze extensive datasets. Key findings revealed higher collision rates in urban counties and rising collision rates in mostly rural areas, where Alive@25 participation is declining. These insights led to recommendations for improving road infrastructure and expanding safety training programs. This research demonstrates the potential of AI-driven insights to inform timely, cost-effective interventions and promote multi-stakeholder engagement in addressing public safety challenges while teaching students data science and AI skills and civic engagement.
      </div>
    </div>
  </div>

  <div class="publication">
    <div class="publication-title">
      On the Books in South Carolina: Mining for Jim Crow Laws
    </div>
    <div class="publication-authors">
      K. Boyd, V. Srivastava, L. DuPre, C. Frear, <b>N. Gupta</b>
    </div>
    <div class="publication-venue">
      University of South Carolina (Feb 2025)
      <a href="https://scholarcommons.sc.edu/lib_facpub/63/" 
         class="publication-link" 
         target="_blank"
         title="View Publication">
        <i class="fas fa-external-link-alt"></i>
      </a>
    </div>
    <div class="abstract-container">
      <input type="checkbox" id="abstract-otb" class="abstract-toggle">
      <label for="abstract-otb" class="abstract-btn">Show Abstract</label>
      <div class="publication-abstract">
        On the Books in South Carolina: Mining for Jim Crow Laws is a collections-as-data and machine learning project by the University of South Carolina Libraries (USC), sub awarded by the University of North Carolina at Chapel Hill (UNC), and made possible by The Andrew W. Mellon Foundation, for the period of May 2022-December 2024. Following UNC’s steps from their first year of the grant, the USC project created a text corpus of South Carolina state legislature acts passed in the period from Reconstruction through the Civil Rights Movement (1868-1968). The USC team then utilized machine learning techniques to create a model classifying the laws as either Jim Crow or not.
      </div>
    </div>
  </div>

</div>
