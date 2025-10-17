---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
~ [[Architect]]  

> [!scale] [[Construir]] | [[Renovar]] — [[Jardineiro]] ⤵️

Quando você tem um mapa de conteúdo mais antigo ou que sente que precisa de algum tipo de atualização, você pode dar a ele a tag `architect/renovate`.  
A visualização a seguir está ordenada pelas notas mais recentemente modificadas.  


```dataview
TABLE WITHOUT ID
	choice(contains(file.tags, "#architect/renovate"),
		"🪜 " + file.link,
	file.link) as "Notes to Architect",
    
    join(filter(file.tags, (t) => startswith(t, "#architect/")), ", ") as "Architect Tags",
    
    choice(contains(file.folder, "+"),
	    "`" + file.folder + "`",
	    regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
		) as "Parent Folder"

FROM #architect/renovate 

WHERE !contains(file.name, "Master Key (Architect Tags)")

SORT file.mtime DESC

LIMIT 77
```

