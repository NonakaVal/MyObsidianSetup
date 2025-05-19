---
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
area: "[[<% tp.file.folder() %>]]"
summary: 
tags: 
---



Summary and Purpose : `INPUT[text(showcase):summary]` - Area Notes Related : `INPUT[inlineListSuggester(optionQuery(#area)):connections]` 

# [[<% tp.file.title %>]]


## Log


---


<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder();
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `area/${task_tag_value}`; 
    }); 
}); -%>


---


Last modified : `$= dv.current().file.mtime`