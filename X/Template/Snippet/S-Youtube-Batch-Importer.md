
<%*
// --- CONFIGURATION ---
const outputFolder = "V-02-Inspiracoes";
// --------------------

const notice = (msg) => new Notice(msg, 10000);

// --- Read all links from the file ---
const fileContent = tp.file.content;
if (!fileContent || fileContent.trim() === "") {
  notice("❌ The file is empty.");
  return;
}
const links = fileContent.split('\n').filter(link => link.trim() !== "");
if (links.length === 0) {
  notice("❌ Could not find any links.");
  return;
}

notice(`▶️ Starting to process ${links.length} links...`);
let createdCount = 0;
let skippedCount = 0;

for (const link of links) {
  // --- 1. FETCH AND PARSE ---
  let doc;
  try {
    // YOUR FIX APPLIED: Use the link directly without splitting it.
    const page = await tp.obsidian.request({ url: link });
    const p = new DOMParser();
    doc = p.parseFromString(page, "text/html");
  } catch (e) {
    notice(`❌ Failed to fetch page for ${link}. Skipping.`);
    skippedCount++;
    continue;
  }

  const $ = (s) => doc.querySelector(s);
  if (!$("meta[name='title']")) {
      notice(`❌ Could not find video data for ${link}. Skipping.`);
      skippedCount++;
      continue;
  }

  // --- 2. EXTRACT AND FORMAT ---
  const title = $("meta[name='title']").content;
  const cleanTitle = title.replaceAll(/[^a-zA-Z0-9 ]/g, "").trim();
  const fileName = `${cleanTitle}.md`;
  const filePath = outputFolder ? `${outputFolder}/${fileName}` : fileName;

  if (app.vault.getAbstractFileByPath(filePath)) {
    skippedCount++;
    continue;
  }

  const shortlinkUrl = $("link[rel='shortlinkUrl']").href;
  const durationStr = $("meta[itemprop='duration']").content.slice(2, -1);
  const uploadDate = $("meta[itemprop='uploadDate']").content;
  const authorName = $("span[itemprop='author'] > link[itemprop='name']").getAttribute("content");

  // Format Duration
  const timeStr = (time) => time.toString().padStart(2, '0');
  let [minutes, seconds] = durationStr.split("M");
  let durationSummary = "Seconds";
  let hours = Math.floor(Number(minutes) / 60);
  minutes = (Number(minutes) % 60);
  if (parseInt(minutes, 10) > 0) { durationSummary = "Minutes"; }
  let formattedDuration = `${timeStr(minutes)}:${timeStr(seconds)}`;
  let yamlDuration = "00:" + formattedDuration;
  if (hours > 0) {
    formattedDuration = `${timeStr(hours)}:` + formattedDuration;
    durationSummary = "Hours";
    yamlDuration = formattedDuration;
  }

  // Format Dates
  const formatDate = (date) => {
    let dateString = new Date(date.split('T')[0]).toDateString();
    let [dayString, month, dayNumber, year] = dateString.split(' ');
    let cleanDayNumber = dayNumber.replace(/^0+/, '');
    return `${month} ${cleanDayNumber}, ${year}`;
  };
  const formatDateToISO = (date) => date.split('T')[0];
  const finalUploadDate = formatDate(uploadDate);
  const isoUploadDate = formatDateToISO(uploadDate);


  // --- 3. BUILD THE NOTE CONTENT STRING ---
 const newNoteContent = `---
aliases: ${title}
channel_name: ${authorName}
duration: ${yamlDuration}
uploaded: ${isoUploadDate}
tags:
  - resources/youtube
dateCreated: '${tp.date.now("YYYY-MM-DD")}'
---

by ${authorName}

${title}

${title} ${formattedDuration} ${durationSummary} / ${finalUploadDate}
`;

  // --- 4. CREATE THE NOTE ---
  try {
    await app.vault.create(filePath, newNoteContent);
    createdCount++;
  } catch (e) {
    notice(`❌ ERROR creating note for ${title}. Aborting.`);
    return;
  }
}

// --- FINAL SUMMARY ---
notice(`✅ Finished! Created ${createdCount} new notes. Skipped ${skippedCount}.`);

// Optional: Clear the queue file after processing
// await app.vault.modify(tp.file.file, "");
%>
