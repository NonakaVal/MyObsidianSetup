---
project: "[[<% tp.file.folder() %>]]"
summary:
tags:
type: project_note
created: '[[<% tp.date.now("YYYY-MM-DD") %>]]'
---




<%*
// Get details about folder (change "Work/Meetings" to desired folder)
const meetingsFolder = "00 Code/Projects";
const meetingsTFolder = tp.app.vault.getAbstractFileByPath(meetingsFolder);
const companies = meetingsTFolder.children.filter(subfolder => subfolder instanceof tp.obsidian.TFolder);
let selectedCompany;

// Prompt user to select company if there are any companies
if (companies.length > 0) {
  selectedCompany = (await tp.system.suggester((company) => company.name, companies))?.name;
}

// If no company selected or no companies to select from, prompt for new company
if (!selectedCompany) {
  selectedCompany = await tp.system.prompt("New company");
}

// Move file to company folder, creating the company folder if needed
await tp.file.move(`${meetingsFolder}/${selectedCompany}/${tp.file.title}`);
-%>

