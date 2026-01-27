---
created: <% tp.date.now("YYYY-MM-DD @ HH:mm") %>
cssclasses:
  - wide-page
tags:
  - calendar/week
---

:LiCalendarCheck2: [[<% tp.date.now("YYYY [Week] WW", -7) %>|↶ Previous Week]] | [[<% tp.date.now("YYYY [Week] WW", 7) %>|Following Week ↷]] 
~<% tp.date.now("YYYY-MM [Week] WW") %>  

<%tp.file.cursor()%>
