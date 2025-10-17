---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
~ [[Jardineiro]]  

> [!trees] [[Plante]] | **[[Cultive]]** | [[Questione]] | [[Replantar]] | [[Revitalizar]] | [[Revisitar]] — [[Arquiteto]] ⤴️  

Se você marcou notas com `#garden/cultivate`, então você quer **desenvolver essas notas ainda mais.**  
Isso pode significar adicionar mais reflexões, contexto, links, fontes ou de alguma forma trazer mais valor a elas.  
Você também pode fazer novas observações — esclarecendo, criticando ou expandindo as ideias dentro delas.  

A visualização a seguir está ordenada pelas notas mais recentemente modificadas.  


```dataview
TABLE WITHOUT ID
    "☘ " + file.link as "Notes to cultivate in the ideaverse",
    
    choice(
        contains(file.folder, "+"),
        "`" + file.folder + "`",
        regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
    ) as "Parent Folder"

FROM #garden/cultivate

SORT file.mtime DESC

WHERE !contains(file.name, "Master Key (Garden Tags)")

LIMIT 77
```
