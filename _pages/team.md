---
title: "FiGra - Team"
layout: gridlay
excerpt: "FiGra: Team members"
sitemap: false
permalink: /team/
---

# Group Members

### Faculty
{% assign number_printed = 0 %}
{% for member in site.data.faculty_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h5>{{ member.name }}</h5>
  <h5>{{ member.info }} </h5>
  <h6> <a href="{{ member.website }}">Personal website</a> </h6>
  <h6>email: <{{ member.email }}></h6>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

### Postdoctoral Researchers

<div class="row">

{% assign sorted_postdoc_members = site.data.postdoc_members | sort: 'name' %}
{% for member in sorted_postdoc_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h5>{{ member.name }}</h5>
  <h6> <a href="{{ member.website }}">Personal website</a> </h6>
  <h6>email: <{{ member.email }}></h6>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

### PhD Students

<div class="row">

{% assign sorted_phd_members = site.data.phd_members | sort: 'name' %}
{% for member in sorted_phd_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h5>{{ member.name }}</h5>
  <h6> <a href="{{ member.website }}">Personal website</a> </h6>
  <h6>email: <{{ member.email }}></h6>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>

### Research Assistants

<div class="row">

{% for member in site.data.ra_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h5>{{ member.name }}</h5>
  <h6> <a href="{{ member.website }}">Personal website</a> </h6>
  <h6>email: <{{ member.email }}></h6>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>


{% if site.data.vr_members.size > 0 %}
### Visiting Researchers

<div class="row">

{% assign sorted_vr_members = site.data.vr_members | sort: 'name' %}
{% for member in sorted_vr_members %}

<div class="col-sm-4 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="50%" style="float: up" />
  <h5>{{ member.name }}</h5>
  <h6> <a href="{{ member.website }}">Personal website</a> </h6>
  <h6>email: <{{ member.email }}></h6>
  <ul style="overflow: hidden"></ul>
</div>

{% endfor %}

</div>
{% endif %}

{% if site.data.alumni.size > 0 %}
###  Alumni
<div class="row">

<div class="col-sm-4 clearfix">
{% for member in site.data.alumni %}

{% if member.website == null %}
  {{ member.name }}, {{ member.year }}. {{ member.next }} 

{% else %}
  <a href="{{ member.website }}">{{ member.name }}</a>, {{ member.year }}. {{ member.next }} 

{% endif %}

{% endfor %}
  
</div>
{% endif %}

