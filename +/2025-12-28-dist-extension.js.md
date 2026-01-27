```js
(() => {
    "use strict";
    var e = {
        265: function (e, t, n) {
            var i =
                    (this && this.__createBinding) ||
                    (Object.create
                        ? function (e, t, n, i) {
                              void 0 === i && (i = n);
                              var o = Object.getOwnPropertyDescriptor(t, n);
                              (o && !("get" in o ? !t.__esModule : o.writable || o.configurable)) ||
                                  (o = {
                                      enumerable: !0,
                                      get: function () {
                                          return t[n];
                                      },
                                  }),
                                  Object.defineProperty(e, i, o);
                          }
                        : function (e, t, n, i) {
                              void 0 === i && (i = n), (e[i] = t[n]);
                          }),
                o =
                    (this && this.__setModuleDefault) ||
                    (Object.create
                        ? function (e, t) {
                              Object.defineProperty(e, "default", { enumerable: !0, value: t });
                          }
                        : function (e, t) {
                              e.default = t;
                          }),
                a =
                    (this && this.__importStar) ||
                    function (e) {
                        if (e && e.__esModule) return e;
                        var t = {};
                        if (null != e)
                            for (var n in e)
                                "default" !== n && Object.prototype.hasOwnProperty.call(e, n) && i(t, e, n);
                        return o(t, e), t;
                    };
            Object.defineProperty(t, "__esModule", { value: !0 }),
                (t.activate = function (e) {
                    const confirmOpen = "Open File in VS Code?",
                        langMap = { py: "python", h: "cpp", rs: "rust", kt: "kotlin", pl: "perl" };

                    const getVaultPath = () =>
                        s.workspace.getConfiguration().get("obsidian-snippets.path");

                    const ensureFolder = async (path) => {
                        const exists = await r.promises
                            .access(path)
                            .then(() => !0)
                            .catch(() => !1);
                        if (!exists) await r.promises.mkdir(path);
                    };

                    const setupObsidianPath = async () => {
                        s.window.showInformationMessage("Setting up Obsidian path...");
                        const res = await s.window.showOpenDialog({
                            canSelectFolders: !0,
                            canSelectMany: !1,
                            canSelectFiles: !1,
                            openLabel: "Select your Obsidian Vault",
                        });
                        if (!res?.[0]) return;

                        const cfg = s.workspace.getConfiguration();
                        await cfg.update(
                            "obsidian-snippets.path",
                            res[0].path.replace("/C:", ""),
                            s.ConfigurationTarget.Global
                        );

                        const vault = String(cfg.get("obsidian-snippets.path"));
                        const snippetsDir = c.join(vault, "+/vscode-Snippets");
                        await ensureFolder(snippetsDir);
                    };

                    const cmdSetup = s.commands.registerCommand("obsidian-snippets.setup", async () => {
                        await setupObsidianPath();
                    });

                    e.subscriptions.push(cmdSetup);

                    e.subscriptions.push(
                        s.commands.registerCommand("obsidian-snippets.copy", async () => {
                            let vault = getVaultPath();
                            if (!vault) {
                                try {
                                    await setupObsidianPath();
                                    vault = getVaultPath();
                                } catch (err) {
                                    console.error(err);
                                }
                            }

                            const snippetsPath = c.join(vault, "+/vscode-Snippets");
                            await ensureFolder(snippetsPath);

                            const editor = s.window.activeTextEditor;
                            const selection = editor?.selection;
                            const code = editor?.document.getText(selection);

                            const ext = c.extname(editor?.document.fileName).slice(1);
                            const lang = langMap[ext] || ext;

                            const folderName = c.basename(c.dirname(editor?.document.fileName));
                            const fileName = c.basename(editor?.document.fileName);

                            const dateStamp = new Date().toISOString().split("T")[0];

                            // NEW: filename with folder + file
                            const outputName = `${dateStamp}-${folderName}-${fileName}.md`;

                            const outputPath = c.join(snippetsPath, outputName);

                            const exists = await r.promises
                                .access(outputPath)
                                .then(() => !0)
                                .catch(() => !1);

                            try {
                                if (exists) {
                                    await r.appendFile(
                                        outputPath,
                                        `\n\n\`\`\`${lang}\n${code}\n\`\`\``,
                                        (e) => e && console.log(e)
                                    );
                                } else {
                                    await r.writeFile(
                                        outputPath,
                                        `\`\`\`${lang}\n${code}\n\`\`\``,
                                        (e) => e && console.log(e)
                                    );
                                }
                            } catch (err) {
                                console.log("Error writing snippet:", err);
                            }

                            const userChoice = await s.window.showInformationMessage(
                                "Snippet copied to Obsidian!",
                                confirmOpen
                            );

                            if (userChoice === confirmOpen) {
                                try {
                                    const doc = await s.workspace.openTextDocument(s.Uri.file(outputPath));
                                    await s.window.showTextDocument(doc);
                                } catch (err) {
                                    console.log(err);
                                }
                            }
                        })
                    );
                }),
                (t.deactivate = function () {});

            const s = a(n(398)),
                r = n(896),
                c = n(928);
        },

        398: (e) => {
            e.exports = require("vscode");
        },
        896: (e) => {
            e.exports = require("fs");
        },
        928: (e) => {
            e.exports = require("path");
        },
    };

    var t = {},
        n = (function n(i) {
            var o = t[i];
            if (void 0 !== o) return o.exports;
            var a = (t[i] = { exports: {} });
            return e[i].call(a.exports, a, a.exports, n), a.exports;
        })(265);

    module.exports = n;
})();

```