---
layout: projects
title: 同好
permalink: /people/
---

<table class="peoplelist">
{% for proj in site.people reversed %}
<tr>
    <td class="peopleimg">
     {%- if proj.imgid -%}
        <img src="/assets/img/{{ proj.imgid }}.jpg" alt="teaser"/>
     {% else %}
     {%- endif -%}
    </td>
    <td class="projtext" id="peopletext">
        <strong><a href="{{proj.link}}">{{ proj.title }}</a></strong> <br>
        <div class='projbutton'>
          <a href="{{site.baseurl}}/tags/#{{proj.tag|slugize}}">本站收录</a>
          {% if proj.link %}| <a href="{{ proj.link }}" target="_blank">个人链接</a>{% endif %}
          {% if proj.lofter %}| <a href="https://{{proj.lofter}}.lofter.com" target="_blank">老福特</a> {% endif %}
          {% if proj.ao3 %} | <a href="https://archiveofourown.org/users/{{proj.ao3}}" target="_blank">AO3</a> {% endif %}
        </div>
    </td>
</tr>
{% endfor %}
</table>
