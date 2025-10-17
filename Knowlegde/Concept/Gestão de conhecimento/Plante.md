---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
tags:
  - garden/revitalize
---
~ [[Jardineiro]]  

> [!trees] [[Plante]] | **[[Cultive]]** | [[Questione]] | [[Replantar]] | [[Revitalizar]] | [[Revisitar]] — [[Arquiteto]] ⤴️  

Se você marcou notas com `#garden/plant`, provavelmente as criou com pressa, mas quer se lembrar de **conectar essas notas ao restante do seu ideaverse.**  

```dataview
TABLE WITHOUT ID
    "🌱 " + file.link as "Notes to plant in the ideaverse",
    
    choice(contains(file.folder, "+"),
	    "`" + file.folder + "`",
	    regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
		) as "Parent Folder"

FROM #garden/plant

SORT file.mtime DESC

WHERE !contains(file.name, "Master Key (Garden Tags)")

LIMIT 77
```

