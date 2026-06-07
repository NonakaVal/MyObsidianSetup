---
dateCreated: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
area:
  - "[[Collectors Guardian]]"
summary: <% tp.system.prompt("summary")%>
tags:
  - <% tp.system.suggester(item => item, Object.keys(tp.app.metadataCache.getTags()).map(x => x.replace("#", "")))%>
type: area_note
subject:
  - "[[hub-work]]"
---
