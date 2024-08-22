---
layout: page
title: Education
---

{% for edu in site.data.resume.education %}
## {{ edu.institution }}
**{{ edu.degree }}** - GPA: {{ edu.gpa }}  
*{{ edu.location }}*  
{{ edu.duration }}

{% for detail in edu.details %}
- {{ detail }}
{% endfor %}

{% endfor %}