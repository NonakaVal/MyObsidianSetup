<%*
const moods = [
  "🙂 – Neutral",
  "😄 – Happy",
  "😐 – Meh",
  "😞 – Sad",
  "😠 – Frustrated"
];

let selectedMood = await tp.system.suggester(mood => mood, moods);
if (!selectedMood) {
  selectedMood = await tp.system.prompt("Type custom mood");
}
-%>
---
dateCreated: <% tp.date.now("YYYY-MM-DD @ HH:mm") %>
tags:
  - dailynote
week: '[[<% tp.date.now("YYYY [Week] WW") %>]]'
daily-mood: "<% selectedMood %>"
---

// Daily quote
<% await tp.web.daily_quote() %>

[[<% tp.date.yesterday("YYYY-MM-DD") %>|↶ Previous Day]] | [[<% tp.date.tomorrow("YYYY-MM-DD") %>|Following Day ↷]]

<% tp.date.now("YYYY-MM-DD") %>’s Note

<%tp.file.cursor()%>






---



# Capture 


