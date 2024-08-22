---
layout: page
title: Experience
---

{% for exp in site.data.resume.experience %}
## {{ exp.title }}
**{{ exp.company }}** - *{{ exp.location }}*  
{{ exp.duration }}

{% for resp in exp.responsibilities %}
- {{ resp }}
{% endfor %}

{% endfor %}