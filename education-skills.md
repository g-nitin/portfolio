---
layout: page
title: Education
---
## Education

{% for edu in site.data.resume.education %}
## {{ edu.institution }}
**{{ edu.degree }}** - GPA: {{ edu.gpa }}  
*{{ edu.location }}*  
{{ edu.duration }}

{% for detail in edu.details %}
- {{ detail }}
{% endfor %}

{% endfor %}

---
## Technical Skills

### Advanced
<div class="skills-container">
{% for skill in site.data.resume.skills.advanced %}
  <a href="{{ skill.url }}" target="_blank" rel="noreferrer" class="skill-icon">
    <img src="{{ skill.icon }}" width="36" height="36" alt="{{ skill.name }}" title="{{ skill.name }}" />
  </a>
{% endfor %}
</div>

### Intermediate
<div class="skills-container">
{% for skill in site.data.resume.skills.intermediate %}
  <a href="{{ skill.url }}" target="_blank" rel="noreferrer" class="skill-icon">
    <img src="{{ skill.icon }}" width="36" height="36" alt="{{ skill.name }}" title="{{ skill.name }}" />
  </a>
{% endfor %}
</div>

---
## Languages

### Native

| {% for lang in site.data.resume.languages.native %}{{ lang }}{% unless forloop.last %} | {% endunless %}{% endfor %}

### Proficient
{% for lang in site.data.resume.languages.proficient %}
| {{ lang }} {% unless forloop.last %} | {% endunless %}{% endfor %}


<!--  -->
<!-- ## Technical Skills

### Advanced
{% for skill in site.data.resume.skills.advanced %}
- {{ skill }}
{% endfor %}

### Intermediate
{% for skill in site.data.resume.skills.intermediate %}
- {{ skill }}
{% endfor %}

---
## Languages

### Native
{% for lang in site.data.resume.languages.native %}
- {{ lang }}
{% endfor %}

### Proficient
{% for lang in site.data.resume.languages.proficient %}
- {{ lang }}
{% endfor %} -->