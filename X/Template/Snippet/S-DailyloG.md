<%*
// --- CONFIGURAÇÃO ---
const dailyNoteFolder = "Daily Notes";
const dailyNoteTemplate = "X/Template/Format/B-Daily Note Template.md";
const captureSection = "# Capture";
// --------------------

// Tipos de capture (label exibido no suggester → [emoji, isTask])
const types = [
  ["🧭 Intenção",    "🧭",  false],
  ["✅ Nova Tarefa", "✅",  true ],
  ["🌱 Motivação",   "🌱",  false],
  ["💬 Gratidão",    "💬",  false],
  ["😴 Even",        "😴",  false],
  ["💀 Puts",        "💀",  false],
  ["⭐ Algo bom",    "⭐",  false],
  ["💩 Cagada",      "💩",  false],
  ["❓ wtf?",        "❓",  false],
];

const notice = (msg) => new Notice(msg, 8000);

// 1. Escolher tipo
const chosen = await tp.system.suggester(
  types.map(t => t[0]),
  types,
  true,
  "Que tipo de capture?"
);
if (!chosen) return;

const [_, emoji, isTask] = chosen;

// 2. Digitar o valor
const value = await tp.system.prompt(`${emoji} ...`);
if (!value || value.trim() === "") return;

// 3. Montar data/hora
const date    = tp.date.now("YYYY-MM-DD");
const time    = tp.date.now("HH:mm");
const dateLink = `[[${date}]]`;

// 4. Montar a linha final
let line;
if (isTask) {
  line = `- [ ] ✅ ${value} - ${time} \\ ${dateLink}`;
} else {
  line = `- ${emoji} ${value} - ${time} \\ ${dateLink}`;
}

// 5. Garantir que a daily note existe
const dailyPath = `${dailyNoteFolder}/${date}.md`;
let dailyFile = app.vault.getAbstractFileByPath(dailyPath);

if (!dailyFile) {
  // Criar a partir do template
  const templateFile = app.vault.getAbstractFileByPath(dailyNoteTemplate);
  if (!templateFile) {
    notice("❌ Template da daily note não encontrado.");
    return;
  }
  const templateContent = await app.vault.read(templateFile);
  dailyFile = await app.vault.create(dailyPath, templateContent);
  // Deixa o Templater processar o arquivo recém-criado se necessário
  await new Promise(r => setTimeout(r, 300));
  dailyFile = app.vault.getAbstractFileByPath(dailyPath);
}

// 6. Ler conteúdo e inserir após a seção # Capture
let content = await app.vault.read(dailyFile);

if (content.includes(captureSection)) {
  // Insere após o cabeçalho, no final do bloco
  const idx = content.indexOf(captureSection) + captureSection.length;
  // Acha o próximo heading ou fim do arquivo
  const afterSection = content.slice(idx);
  const nextHeading  = afterSection.search(/\n#+ /);
  
  if (nextHeading === -1) {
    // Não tem próximo heading — insere no fim
    content = content + "\n" + line;
  } else {
    // Insere antes do próximo heading
    const insertAt = idx + nextHeading;
    content = content.slice(0, insertAt) + "\n" + line + content.slice(insertAt);
  }
} else {
  // Seção não existe — cria no final
  content = content + "\n" + captureSection + "\n" + line;
}

await app.vault.modify(dailyFile, content);
notice(`${emoji} Capture salvo na daily ${date}`);
%>