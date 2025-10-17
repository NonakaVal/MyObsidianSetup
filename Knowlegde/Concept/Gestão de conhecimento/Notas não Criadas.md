---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
~ [[Adicionar]]  

Nunca comece com uma página em branco. Surpreenda-se com o trabalho que você já fez invisivelmente.  

Esta visualização avançada mostra **notas de espaço reservado que estão se acumulando** com pelo menos `3` links apontando para elas.  
Se você sentir o estalo, transforme a nota de espaço reservado em uma nota real.  


```dataviewjs
const count = 3;
let d = {};
function process(k, v) {
  Object.keys(v).forEach(function (x) {
    x = dv.fileLink(x);
    if (d[x]==undefined) { d[x] = []; }
    d[x].push(dv.fileLink(k));
  });
}

Object.entries(dv.app.metadataCache.unresolvedLinks)
    .filter(([k,v])=>Object.keys(v).length)
    .forEach(([k,v]) => process(k, v));
    
dv.table(["Notas não Criadas", "Apontadas por"],
         Object.entries(d)
         .filter(([k, v]) => v.length >= count)
         .sort((b, a) => b[1].length - a[1].length)
         .map(([k,v])=> [k, v.join(" • ")]))
```
