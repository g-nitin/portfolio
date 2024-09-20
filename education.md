---
layout: page
title: Education
---
---
# Education

{% for edu in site.data.resume.education %}
## {{ edu.institution }}
**{{ edu.degree }}** - GPA: {{ edu.gpa }}  
*{{ edu.location }}*  
{{ edu.duration }}

{% for detail in edu.details %}
- {{ detail }}
{% endfor %}

{% endfor %}
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