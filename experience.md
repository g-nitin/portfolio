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

**Related Links:** 
{% if exp.links %}
| {% for link in exp.links %}[{{ link.text }}]({{ link.url }}){% unless forloop.last %} | {% endunless %}{% endfor %}
{% endif %}

{% endfor %}