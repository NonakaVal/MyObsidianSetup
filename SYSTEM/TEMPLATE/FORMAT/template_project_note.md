---
project: <% tp.file.folder() %>
summary: 
tags: 
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
---

# Set first

Summary and Purpose : `INPUT[text(showcase):summary]`

Select Connection: `INPUT[inlineListSuggester(optionQuery(#project), optionQuery(#area)):connections]` 

# Log




<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const task_tag_value = tp.file.folder();
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["tags"] = `project/${task_tag_value}`; 
    }); 
}); -%>
