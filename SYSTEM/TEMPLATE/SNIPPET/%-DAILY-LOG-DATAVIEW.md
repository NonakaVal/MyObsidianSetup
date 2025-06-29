
```js
// 📅 Define date range
const startDate = new Date("2024-06-01");
const endDate = new Date("2025-06-16");

// Load and filter pages by date
const pages = dv.pages('#calendar/daily')
    .where(p => {
        const fileDate = new Date(p.file.name);
        return fileDate >= startDate && fileDate <= endDate;
    })
    .sort(p => p.file.name, 'desc');

const headName = "Daily LOG";
let tableRows = [];

// Define array of exclusion regex patterns
const excludePatterns = [
    /\[\[Recording\s\d{14}(\.m4a)?\]\]/, // Wikilinks de gravações
    /\[.*?\]\(obsidian:\/\/swiftink_transcript_functions\?id=[\w-]+\)/, // Links Swiftink
    /INPUT\[.*?option\(.*?\).*?\]/, // Componentes INPUT[...] com opções
    /Áudio do WhatsApp de \d{4}-\d{2}-\d{2} à\(s\) \d{2}\.\d{2}\.\d{2}_[\w\d]+\.waptt\.opus/ // Áudios do WhatsApp
];

for (const page of pages) {
    const content = await dv.io.load(page.file.path);
    const lines = content.split('\n');
    let insideHead = false;
    let sectionContent = [];

    for (const line of lines) {
        if (line.startsWith("# " + headName)) {
            insideHead = true;
            continue;
        }
        if (line.startsWith("# ") && insideHead) {
            break;
        }
        if (insideHead) {
            const trimmedLine = line.trim();

            // Check against all exclusion patterns
            if (excludePatterns.some(pattern => pattern.test(trimmedLine))) continue;

            sectionContent.push(trimmedLine);
        }
    }

    if (sectionContent.length > 0) {
        tableRows.push([
            page.file.link,
            sectionContent.join('\n')
        ]);
    }
}

dv.table(["🗓️ Data", "📝 Conteúdo"], tableRows);

```