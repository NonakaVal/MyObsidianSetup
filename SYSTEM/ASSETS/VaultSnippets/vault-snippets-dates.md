---
tags:
  - resources
---


# created note link templater

## templater
```
<% tp.file.creation_date() %>
```

## native to properties

```
'[[{{date}}]]'
```

# Last modified link note

```
=link(dateformat(date(today), "yyyy-MM-dd"))
```

```
Last modified :   `="[[" + dateformat(date(today), "yyyy-MM-dd") + "]]"` - `$= dv.current().file.mtime`
```

```
Last modified : `$= dv.current().file.mtime`
```