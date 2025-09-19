 `BUTTON[<% tp.system.prompt("id")%>]`     

```meta-bind-button
label: <% tp.system.prompt("Label")%>
hidden: true
icon: <% tp.system.prompt("icon")%>
class: ""
id: <% tp.system.prompt("id")%>
style: <% tp.system.prompt("style")%>
actions:
  - type: command
    command: <% tp.system.clipboard() %>
```

