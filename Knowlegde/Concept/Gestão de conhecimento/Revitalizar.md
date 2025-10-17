---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
> [!trees] [[Plante]] | **[[Cultive]]** | [[Questione]] | [[Replantar]] | [[Revitalizar]] | [[Revisitar]] — [[Arquiteto]] ⤴️  

Se você marcou notas com `#garden/revitalize`, então você quer **revisar essas notas de uma forma que lhes dê nova vida.** Frequentemente é aquela sensação de que algo está preso na nota e, se você apenas reescrevê-la ou reestruturá-la, isso proporcionará mais clareza e valor.

A visualização a seguir está ordenada pelas notas mais recentemente modificadas.


```dataview
TABLE WITHOUT ID
    "💦 " + file.link as "Notes to revitalize in the ideaverse",
    
    choice(
        contains(file.folder, "+"),
        "`" + file.folder + "`",
        regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
    ) as "Parent Folder"

FROM #garden/revitalize

SORT file.mtime DESC

WHERE !contains(file.name, "Master Key (Garden Tags)")

LIMIT 77
```
