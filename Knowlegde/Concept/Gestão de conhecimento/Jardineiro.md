---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---

> [!trees] [[Plante]] | **[[Cultive]]** | [[Questione]] | [[Replantar]] | [[Revitalizar]] | [[Revisitar]] — [[Arquiteto]] ⤴️  

Quando você estiver em uma nota e sentir que quer voltar a ela, basta adicionar a tag `garden` nessa nota.  
Não importa se você tem um motivo claro ou apenas uma sensação vaga.  
Depois, por meio das seguintes visualizações do Garden, você poderá encontrá-la novamente (e criar conexões serendipitosas pelo caminho).  

Chaves : 🌱 Plant | ☘️ Cultivate | 🪴 Repot | 🍄 Question | 💦 Revitalize | 🍁 Revisit
```dataview
TABLE WITHOUT ID
	choice(contains(file.tags, "#garden/plant"),
        "🌱 " + file.link,
	choice(contains(file.tags, "#garden/cultivate"),
		"☘️ " + file.link,
	choice(contains(file.tags, "#garden/question"),
		"🍄 " + file.link,
	choice(contains(file.tags, "#garden/repot"),
		"🪴 " + file.link,
	choice(contains(file.tags, "#garden/revitalize"),
		"💦 " + file.link,
	choice(contains(file.tags, "#garden/revisit"),
		"🍁 " + file.link,
	file.link)))))) as "Notes to Garden",
    
    join(filter(file.tags, (t) => startswith(t, "#garden/")), ", ") as "Garden Tags",
    
    choice(contains(file.folder, "+"),
	    "`" + file.folder + "`",
	    regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
		) as "Parent Folder"

FROM #garden

WHERE !contains(file.name, "Master Key (Garden Tags)")

SORT file.mtime DESC

LIMIT 77
```
