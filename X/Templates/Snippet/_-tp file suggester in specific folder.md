<%*
const folder = "";
const items = tp.app.vault.getMarkdownFiles().filter(x => x.path.startsWith(folder));
const selectedItem = (await tp.system.suggester((item) => item.basename, items)).basename;
-%>


[[<% selectedItem %>]]
