~~~dataview
TABLE WITHOUT ID
	choice(contains(file.tags, "#garden/seed"),
        "🫘" + file.link,
	choice(contains(file.tags, "#garden/plant"),
        "🌱 " + file.link,
	choice(contains(file.tags, "#garden/cultivate"),
		"☘️ " + file.link,
	choice(contains(file.tags, "#garden/question"),
		"🍄 " + file.link,
	choice(contains(file.tags, "#garden/repot"),
		"🪴 " + file.link,
	choice(contains(file.tags, "#garden/revitalize"),
		"💦 " + file.link,
	choice(contains(file.tags, "#garden/revisit"),
		"🍁 " + file.link,
	file.link))))))) as "Notes",
    
    join(filter(file.tags, (t) => startswith(t, "#garden/")), ", ") as "Tags",
    
    choice(contains(file.folder, "+"),
	    "`" + file.folder + "`",
	    regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
	) as "Folder"

FROM #garden
WHERE !contains(file.path, "30 Knowlegde/35 Recources/Ideaverse Pro 2") AND !contains(file.path, "System")
AND !contains(file.name, "Master Key (Garden Tags)")

SORT file.mtime DESC
LIMIT 77

~~~

[^1]

[^1]: 🫘Seed | 🌱 Plant | ☘️ Cultivate 
	🪴 Repot | 🍄 Question | 💦 Revitalize | 🍁 Revisit
