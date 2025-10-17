---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
> [!scale] [[Construir]] | [[Renovar]] — [[Jardineiro]] ⤵️

Quando você tiver um **mapa de conteúdo que precisa de ajustes**, pode adicionar a tag `architect` nessa nota. Assim, através das **visões de Arquiteto** abaixo, você poderá encontrá-la no momento certo.

**Chave:** 🧱 Construir | 🪜 Renovar  


```dataview
TABLE WITHOUT ID
	choice(contains(file.tags, "#architect/build"),
        "🧱 " + file.link,
	choice(contains(file.tags, "#architect/renovate"),
		"🪜 " + file.link,
	file.link)) as "Notes to Architect",
    
    join(filter(file.tags, (t) => startswith(t, "#architect/")), ", ") as "Architect Tags",
    
    choice(contains(file.folder, "+"),
	    "`" + file.folder + "`",
	    regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
		) as "Parent Folder"

FROM #architect

WHERE !contains(file.name, "Master Key (Architect Tags)")

SORT file.mtime DESC

LIMIT 77
```
