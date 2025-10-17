---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
~ [[Jardineiro]]

> [!trees] [[Plante]] | **[[Cultive]]** | [[Questione]] | [[Replantar]] | [[Revitalizar]] | [[Revisitar]] — [[Arquiteto]] ⤴️  

Se você marcou notas com `#garden/question`, então você quer **refletir sobre as questões nessas notas.** Isso pode significar usar as perguntas como inspiração ou refletir e ruminar mais profundamente sobre os pensamentos que essas questões provocam.


```dataview
TABLE WITHOUT ID
    "🍄 " + file.link as "Notes with questions in the ideaverse",
    
    choice(
        contains(file.folder, "+"),
        "`" + file.folder + "`",
        regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
    ) as "Parent Folder"

FROM #garden/question

SORT file.mtime DESC

WHERE !contains(file.name, "Master Key (Garden Tags)")

LIMIT 77
```
