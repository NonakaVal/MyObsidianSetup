

<%* tp.hooks.on_all_templates_executed(async () => { 
    const file = tp.file.find_tfile(tp.file.path(true)); 
    const date = tp.date.now("YYYY-MM-DD")
    await app.fileManager.processFrontMatter(file, (frontmatter) => { 
        frontmatter["created"] = `[[{date}]]`; 
    }); 
}); -%>


