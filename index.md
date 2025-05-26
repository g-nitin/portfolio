---
layout: default
title: Home
---

<div class="main-content">
  <header class="hero-section">
    <h1 class="hero-title">Welcome to My Portfolio</h1>
    <div class="hero-content">
      <p class="hero-text">
        Hello! I'm Nitin Gupta, a Computer Science Master's student at the University of South Carolina. This portfolio showcases my education, skills, experience, and projects. Feel free to explore and learn more about my journey in the world of technology and software development.
      </p>
    </div>
  </header>

  <section class="about-section">
    <h2 class="section-title">About Me</h2>
    <div class="section-content">
      <p>
        I'm passionate about artificial intelligence, data science, and software engineering. With a strong foundation in computer science and mathematics, I strive to create innovative solutions to real-world problems.
      </p>
    </div>
  </section>

  <div class="news-section">
    <h2 class="news-title">Recent Updates</h2>
    <div class="news-scroll-container">
      <div class="news-grid">

          <div class="news-item">
              <div class="news-date">May 2025</div>
              <span class="news-category category-education">Education</span>
              <div class="news-headline">Graduation!</div>
              <p class="news-description">Grateful to announce that I have completed my undergraduate studies. Recently graduated in May 2025 with major in computer science and minors in data science and mathematics.</p>
          </div>

          <div class="news-item">
              <div class="news-date">March 2025</div>
              <span class="news-category category-publication">Publication</span>
              <div class="news-headline">New Paper Accepted at ICAPS 2025</div>
              <p class="news-description">Our work on revisiting LLMs in planning through a semi-automated analysis of evolving literature categories has been accepted at ICAPS 2025.</p>
              <a href="{{ site.baseurl }}/publications" class="news-link">Read more <i class="fas fa-arrow-right"></i></a>
          </div>

          <div class="news-item">
              <div class="news-date">October 2024</div>
              <span class="news-category category-publication">Publication</span>
              <div class="news-headline">New Paper Accepted at AAAI 2025</div>
              <p class="news-description">Our work on enhancing road safety in South Carolina has been accepted as a Student Abstract at AAAI 2025 in Philadelphia, USA</p>
              <a href="{{ site.baseurl }}/publications" class="news-link">Read more <i class="fas fa-arrow-right"></i></a>
          </div>

          <div class="news-item">
            <div class="news-date">October 2024</div>
            <span class="news-category category-publication">Publication</span>
            <div class="news-headline">New Paper Accepted at CODS COMAD 2024</div>
            <p class="news-description">Our work developing a Planning Ontology has been accepted at CODS COMAD 2024 in India</p>
            <a href="{{ site.baseurl }}/publications" class="news-link">Read more <i class="fas fa-arrow-right"></i></a>
        </div>

          <!-- Experience Update -->
          <div class="news-item">
              <div class="news-date">August 2024</div>
              <span class="news-category category-experience">Experience</span>
              <div class="news-headline">Started Research Assistantship</div>
              <p class="news-description">Joined the AI4Society Lab as an Undergraduate Research Assistant.</p>
              <a href="{{ site.baseurl }}/experience" class="news-link">View details <i class="fas fa-arrow-right"></i></a>
          </div>

          <!-- Project Update -->
          <!-- <div class="news-item"> -->
              <!-- <div class="news-date">January 2024</div> -->
              <!-- <span class="news-category category-project">Project</span> -->
              <!-- <div class="news-headline">Launched ML Model Deployment Tool</div> -->
              <!-- <p class="news-description">Released a new tool for streamlining machine learning model deployments.</p> -->
              <!-- <a href="{{ site.baseurl }}/projects" class="news-link">Learn more <i class="fas fa-arrow-right"></i></a> -->
          <!-- </div> -->
      </div>
    </div>
  </div>

  <section class="resume-section">
    <h2 class="section-title">Résumé</h2>
    <p>For a quick overview about me, download my résumé.</p>
    <a href="https://g-nitin.github.io/portfolio/assets/Nitin_Gupta_Résumé.pdf" class="resume-btn">
      <i class="fas fa-file-pdf"></i> Download Résumé (PDF)
    </a>
  </section>

  <footer class="site-footer">
    <p>
      <small><i>The source code for this website can be found 
        <a href="https://github.com/g-nitin/portfolio" target="_blank">here</a>. It was built upon the 
        <a href="https://github.com/poole/hyde" target="_blank">Hyde theme by Mark Otto</a>.
      </i></small>
    </p>
  </footer>
</div>
