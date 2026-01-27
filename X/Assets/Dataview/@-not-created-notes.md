~~~dataviewjs
//-----------------------------------------------------------
// 🧩 DETECTOR DE LINKS NÃO CRIADOS (com exclusões)
//-----------------------------------------------------------

const count = 2;
let d = {};

// 🧱 Pastas a serem ignoradas (adicione aqui outras se quiser)
const ignoredFolders = ["X"];

// Função para verificar se um caminho pertence a alguma pasta ignorada
function isIgnored(path) {
  return ignoredFolders.some(folder => path.toLowerCase().includes(folder.toLowerCase()));
}

// Verifica se um link vem de propriedades YAML
function linkInFrontmatter(file, link) {
  const cache = app.metadataCache.getCache(file);
  if (!cache || !cache.frontmatterLinks) return false;
  return cache.frontmatterLinks.some(l => l.link === link);
}

function process(k, v) {
  if (isIgnored(k)) return; // Ignorar notas da lista

  Object.keys(v).forEach(function (x) {
    if (isIgnored(x)) return;            // Ignorar links de pastas ignoradas
    if (linkInFrontmatter(k, x)) return; // Ignorar links vindos do YAML

    if (!d[x]) d[x] = [];
    d[x].push(dv.fileLink(k));
  });
}

// Filtrar e processar apenas notas válidas
Object.entries(dv.app.metadataCache.unresolvedLinks)
  .filter(([k, v]) => !isIgnored(k) && Object.keys(v).length)
  .forEach(([k, v]) => process(k, v));

// Gerar tabela final
dv.table(
  ["Notas não Criadas", "Apontadas por"],
  Object.entries(d)
    .filter(([k, v]) => v.length >= count)
    .sort((a, b) => b[1].length - a[1].length)
    .map(([k, v]) => [dv.fileLink(k), v.join(" • ")])
);

~~~
