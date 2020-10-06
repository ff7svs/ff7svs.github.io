---
layout: projects
title: 友情链接
permalink: /links/
---

<table class="projlist">
{% for proj in site.links reversed %}
<tr>
    <td class="projimg">
     {%- if proj.image -%}
        <img src="{{ proj.image }}" alt="teaser"/>
     {% else %}
        <img src="/assets/img/{{ proj.linkid }}.jpg" alt="teaser"/>
     {%- endif -%}
    </td>
    <td class="projtext">
        <strong><a href="{{proj.link}}">{{ proj.title }}</a></strong> <br>
        By <span>{{ proj.author}}</span> <br>
        <div class='projbutton'>
          {% if proj.page %} | <a href="{{proj.page}}" target="_blank">project webpage</a> {% endif %}
          <a href="javascript:toggleblock('{{proj.linkid}}-abs')">简介</a>
        </div>
        <p class='excerpt'>
            <i id='{{proj.linkid}}-abs' style="display:none;"> {{proj.excerpt}}</i>
        </p>
    </td>
</tr>
{% endfor %}
</table>
