```dataviewjs
const startDate = moment('<% tp.system.prompt("StartDate (YYYY-MM-DD)")%>', 'YYYY-MM-DD');
const endDate = moment('<% tp.date.now("YYYY-MM-DD") %>', 'YYYY-MM-DD');

const pages = dv.pages('#calendar/daily')
    .where(p => {
        const fileDate = moment(p.file.name, "YYYY-MM-DD");
        return fileDate.isBetween(startDate, endDate, null, '[]');
    })
    .sort(p => p.file.name, '<% tp.system.prompt("asc or desc")%>');

const headName = "Logs";
let tableRows = [];

const excludePatterns = [
    /\[\[Recording\s\d{14}(\.m4a)?\]\]/,
    /\[.*?\]\(obsidian:\/\/swiftink_transcript_functions\?id=[\w-]+\)/,
    /INPUT\[.*?option\(.*?\).*?\]/,
    /Áudio do WhatsApp de \d{4}-\d{2}-\d{2} à\(s\) \d{2}\.\d{2}\.\d{2}_[\w\d]+\.waptt\.opus/
];

for (const page of pages) {
    const content = await dv.io.load(page.file.path);
    const lines = content.split('\n');
    let insideHead = false;
    let sectionContent = [];

    for (const line of lines) {
        if (line.startsWith("# " + headName)) { insideHead = true; continue; }
        if (line.startsWith("# ") && insideHead) break;
        if (insideHead) {
            const trimmedLine = line.trim();
            if (excludePatterns.some(pattern => pattern.test(trimmedLine))) continue;
            sectionContent.push(trimmedLine);
        }
    }

    if (sectionContent.length > 0) {
        tableRows.push([
            page.file.link,
            sectionContent.join('<li>')
        ]);
    }
}

dv.table(["🗓️ Data", "📝 Conteúdo"], tableRows);

```
