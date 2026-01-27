%*
const items = tp.app.vault.getMarkdownFiles();
const selectedItem = await tp.system.suggester(item => item.basename, items);
if (selectedItem) {
  const link = tp.app.fileManager.generateMarkdownLink(selectedItem, tp.file.folder(true));
  tR += link;
}
-%>
