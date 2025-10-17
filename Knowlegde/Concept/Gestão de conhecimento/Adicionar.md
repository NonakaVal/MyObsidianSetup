---
up: "[[Mapa de Gestão de Conhecimento|Mapa de Gestão de Conhecimento]]"
collection: "[[SISTEMA/COLEÇÕES/Gestão de Conhecimento.md|Gestão de Conhecimento]]"
---
| `Up` | `INPUT[suggester(optionQuery("")):up]`    | `Coleção` | `INPUT[suggester(optionQuery("Sistema/Coleções")):collection]` 

> [!tldr] [[ARC Framework]] » **[[Adicionar]]** | [[Relacionar]] | [[Comunicar]] 

Esta nota não é apenas uma caixa de entrada. É uma base de resfriamento 🧊. Os pensamentos chegam quentes. Mas depois de alguns dias, eles esfriam. Quando pensamentos mais frios prevalecem, você pode priorizar melhor. Legal? 

Esta visão mostra as 10 notas mais novas na sua pasta `+`. Ao processar cada nota, tente escrever algo com suas próprias palavras e vinculá-la a outra nota. Então, você pode mover a nota para a melhor pasta, e provavelmente nunca mais precisará movê-la novamente.  

``` dataview
TABLE WITHOUT ID
  file.link as "Notas adicionadas mais recentes",
  (date(today) - file.cday).day as "Dias de vida"
FROM "" AND !"Atlas/+"
WHERE regexmatch(".*\\+.*", file.folder)
SORT file.cday desc
LIMIT 33

```


---

Se você quiser encontrar coisas novas, confira: [🐦](https://www.twitter.com) ou [📚](https://readwise.io/lyt/).  

---

Para descobrir notas placeholders com muitos links já existentes, vá para [[Acúmulo de Ideias]]