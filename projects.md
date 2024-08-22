---
layout: page
title: Projects
---

{% for project in site.data.resume.projects %}
## {{ project.name }}
[GitHub Repository]({{ project.github }})

{% for desc in project.description %}
- {{ desc }}
{% endfor %}

{% endfor %}