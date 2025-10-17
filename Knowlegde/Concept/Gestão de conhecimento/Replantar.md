---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
~ [[Jardineiro]]

> [!trees] [[Plante]] | **[[Cultive]]** | [[Questione]] | [[Replantar]] | [[Revitalizar]] | [[Revisitar]] — [[Arquiteto]] ⤴️  

Se você marcou notas com `#garden/repot`, então você quer **refatorar essas notas dividindo ou reformatando-as.** Isso geralmente envolve cortar uma seção específica de uma nota diária e colar o conteúdo em uma nova nota com um título claro.


```dataview
TABLE WITHOUT ID
    "🪴 " + file.link as "Notes to repot in the ideaverse",
    
    choice(
        contains(file.folder, "+"),
        "`" + file.folder + "`",
        regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
    ) as "Parent Folder"

FROM #garden/repot

WHERE !contains(file.name, "Master Key (Garden Tags)")

SORT file.mtime DESC

LIMIT 77
```
