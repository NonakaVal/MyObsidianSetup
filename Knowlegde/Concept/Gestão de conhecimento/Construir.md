---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
~ [[Arquiteto]] 

> [!scale] [[Construir]] | [[Renovar]] — [[Jardineiro]] ⤵️

Quando você tem um **mapa de conteúdo novo ou inacabado** que ainda precisa de atenção, atribua a tag `#architect/build`.  
A visualização abaixo mostra essas notas, ordenadas pelas **mais recentemente modificadas**:

```dataview
TABLE WITHOUT ID
    "🧱 " + file.link as "Notes to build in the ideaverse",
    
    choice(contains(file.folder, "+"),
	    "`" + file.folder + "`",
	    regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
		) as "Parent Folder"

FROM #architect/build 

SORT file.mtime DESC

WHERE !contains(file.name, "Master Key (Architect Tags)")

LIMIT 77
```