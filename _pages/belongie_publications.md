---
title: "FiGra - Publications"
layout: gridlay
excerpt: "FiGra -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

This page currentely contains the publications of [belongielab.org/](https://www.belongielab.org/)


[Google Scholar](https://scholar.google.com/citations?user=chD5XxkAAAAJ)


{% for pub_year in site.data.pubyears %}

<h3 style="padding-bottom: 0px;margin-bottom: 0; text-align: center;">{{ pub_year }}</h3>
<hr style="border: 2;height: 2px;width: 90%;" />


{% for publi in site.data.publist %}

{% if publi.year == pub_year %}

{% if publi.note == null %}

  {{ publi.author }} <br />
  <b> {{ publi.title }} </b> <br />
  {{ publi.venue }} {{ publi.year }}. <br />
  <a href="{{ publi.link.url }}">[{{ publi.link.display }}]</a>

{% else %}

  {{ publi.author }} <br />
  <b> {{ publi.title }} </b> <br />
  {{ publi.venue }} {{ publi.year }}{{ publi.note }}. <br />
  <a href="{{ publi.link.url }}">[{{ publi.link.display }}]</a>

{% endif %}

<!-- {% if publi.link.url != null %}
  <a href="{{ publi.link.url }}">[{{ publi.link.display }}]</a>
{% endif %}
 -->
{% endif %}

{% endfor %}

{% endfor %}

