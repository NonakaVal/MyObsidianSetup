---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
~ [[Jardineiro]]

> [!trees] [[Plante]] | **[[Cultive]]** | [[Questione]] | [[Replantar]] | [[Revitalizar]] | [[Revisitar]] — [[Arquiteto]] ⤴️  

Se você marcou notas com `#garden/revisit`, então você quer **relê-las.**  
Talvez queira um lembrete, um reforço, ou simplesmente reler por qualquer motivo, pois você sabe que nem tudo que brilha é ouro e algumas das notas mais antigas contêm os maiores tesouros.


```dataview
TABLE WITHOUT ID
    "🍁 " + file.link as "Notes to revisit in the ideaverse",
    
    choice(
        contains(file.folder, "+"),
        "`" + file.folder + "`",
        regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
    ) as "Parent Folder"

FROM #garden/revisit

SORT file.mtime DESC

WHERE !contains(file.name, "Master Key (Garden Tags)")

LIMIT 77
```
