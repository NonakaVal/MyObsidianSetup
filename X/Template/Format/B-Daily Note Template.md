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
  - calendar/daily
week: '[[<% tp.date.now("YYYY [Week] WW") %>]]'
daily-mood: "<% selectedMood %>"
---
<% tp.date.now("YYYY-MM-DD") %>’s Note
[[<% tp.date.yesterday("YYYY-MM-DD") %>|↶ Previous Day]] | [[<% tp.date.tomorrow("YYYY-MM-DD") %>|Following Day ↷]]

<%*
  const elixirConfDate = new Date('2026-06-14');
  const now = new Date();
  const diff = elixirConfDate - now;
  const days = Math.floor(diff / (1000 * 3600 * 24));
%># Faltam <font color="red"> <% days %></font>  dias - [[Planejamento Aniversário bb]]



// Daily quote
<% await tp.web.daily_quote() %>



<%tp.file.cursor()%>

---



# Capture 


