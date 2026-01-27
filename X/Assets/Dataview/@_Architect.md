~~~dataview
TABLE WITHOUT ID
	choice(contains(file.tags, "#architect/build"),
        "🧱 " + file.link,
	choice(contains(file.tags, "#architect/renovate"),
		"🪜 " + file.link,
	file.link)) as "Notes",
    
    join(filter(file.tags, (t) => startswith(t, "#architect/")), ", ") as "Tags",
    
    choice(contains(file.folder, "+"),
	    "`" + file.folder + "`",
	    regexreplace(file.path, ".*/([^/]+)/[^/]+$", "$1")
		) as "Folder"

FROM #architect and -"30 Knowlegde/35 Recources/Ideaverse Pro 2"

WHERE !contains(file.name, "Master Key (Architect Tags)")

SORT file.mtime DESC

LIMIT 77
~~~

[^1]

[^1]: 🧱 Build | 🪜 Renovate
