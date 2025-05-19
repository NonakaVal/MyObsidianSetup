---
tags:
  - resources
---


# created note link templater

## templater
```
2025-05-19 03:52
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