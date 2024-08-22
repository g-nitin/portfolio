---
layout: page
title: Skills
---

## Technical Skills

### Advanced
{% for skill in site.data.resume.skills.advanced %}
- {{ skill }}
{% endfor %}

### Intermediate
{% for skill in site.data.resume.skills.intermediate %}
- {{ skill }}
{% endfor %}

## Languages

### Native
{% for lang in site.data.resume.skills.languages.native %}
- {{ lang }}
{% endfor %}

### Proficient
{% for lang in site.data.resume.skills.languages.proficient %}
- {{ lang }}
{% endfor %}