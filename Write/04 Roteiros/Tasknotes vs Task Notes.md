---
tags:
status: approved
summary: " tasknotes e taskgenius."
rank: 5
chance: 3
area:
  - "[[Val Channel]]"
subject:
  - "[[hub-work]]"
  - "[[hub-pkm]]"
---
# Introdução 

If you really don't want to use plugins for this, you can either use search `task:""` in the side-bar or you can do an [embedded search query](<https://help.obsidian.md/plugins/search#Embed+search+results+in+a+note>) to pull that search into a central page. 

Query to pull all tasks regardless of status (includes done and special custom checkboxes such as `- [b]`): 




Or for **regular tasks** that are **not done** you would put in. 
`task-todo:""`  or you could put `" - [ ]"`

For **done** tasks (including special checkboxes like `- [b]`) 
`task-done:""`

For ONLY **regular done tasks** (only relevant if you utilise special checkboxes) you would put
`"- [x]"`

You won't have as fine control as you would with a plugin, and you will need to go to individual pages to delete/check off (or use page-preview) but you can add things like path and tag underneath, 

```
```query
task:#Books
path:folder
```
or search for a specific date etc
`task:2025-10-05`

Utilise the [search operators](<https://help.obsidian.md/plugins/search#Search+operators>) to refine.


 em um dos meus vídeos sobre plugins da comunidade eu recomendei um plugin chamado checklist no qual sua função é centralizar suas tasks classificadas por tags específicas. 
 de fato se trata de um dos plugins mais úteis quando se fala de gestão de tasks... mas hoje eu quero adentrar um pouco mais essa questão...

hoje vim apresentar dois dos melhores plugins que testei, tasknotes e taskgenius.

````tabs
tab: tasknotes

https://github.com/callumalpass/tasknotes

<iframe 
  src="https://github.com/callumalpass/tasknotes" 
  width="100%" 
  height="600" 
  frameborder="0"
  style="border:1px solid #ccc;">
</iframe>


tab: taskgenius

https://github.com/Quorafind/Obsidian-Task-Genius
[[taskgenius]]/

<iframe 
  src="https://github.com/Quorafind/Obsidian-Task-Genius" 
  width="100%" 
  height="600" 
  frameborder="0"
  style="border:1px solid #ccc;">
</iframe>


````



# Taskgenius

começando com um que descobri bem recentemente abrindo uma discussão no reddit, não importa o assunto sempre q faço isso dá muito bom, mas focando no plugin