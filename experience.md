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

{% if exp.links %}
**Related Links:** 

| {% for link in exp.links %}[{{ link.text }}]({{ link.url }}){% unless forloop.last %} | {% endunless %}{% endfor %}
{% endif %}

---

{% endfor %}