'use strict';

var obsidian = require('obsidian');

/*! *****************************************************************************
Copyright (c) Microsoft Corporation.

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
***************************************************************************** */
/* global Reflect, Promise */

var extendStatics = function(d, b) {
    extendStatics = Object.setPrototypeOf ||
        ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
        function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
    return extendStatics(d, b);
};

function __extends(d, b) {
    if (typeof b !== "function" && b !== null)
        throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
    extendStatics(d, b);
    function __() { this.constructor = d; }
    d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
}

var HotkeysPlus = /** @class */ (function (_super) {
    __extends(HotkeysPlus, _super);
    function HotkeysPlus() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    HotkeysPlus.prototype.onload = function () {
        var _this = this;
        console.log('Loading Hotkeys++ plugin');
        this.addCommand({
            id: 'better-toggle-todo',
            name: 'Toggle to-do lists',
            callback: function () { return _this.toggleTodos(); },
            hotkeys: [
                {
                    modifiers: ['Mod'],
                    key: 'm',
                },
            ],
        });
        this.addCommand({
            id: 'toggle-bullet-number',
            name: 'Toggle line to bulleted or numbered lists',
            callback: function () { return _this.toggleLists(); },
            hotkeys: [
                {
                    modifiers: ['Mod', 'Shift'],
                    key: 'm',
                },
            ],
        });
        this.addCommand({
            id: 'toggle-block-quote',
            name: 'Toggle line to block quote',
            callback: function () { return _this.toggleBlockQuote(); },
            hotkeys: [
                {
                    modifiers: ['Mod'],
                    key: '<',
                },
            ],
        });
        this.addCommand({
            id: 'toggle-embed',
            name: 'Toggle line to embed internal links',
            callback: function () { return _this.toggleEmbed(); },
            hotkeys: [
                {
                    modifiers: ['Mod', 'Shift'],
                    key: '1',
                },
            ],
        });
        this.addCommand({
            id: 'duplicate-lines-down',
            name: 'Copy line(s) down',
            callback: function () { return _this.duplicateLines('down'); },
        });
        this.addCommand({
            id: 'duplicate-lines-up',
            name: 'Copy line(s) up',
            callback: function () { return _this.duplicateLines('up'); },
        });
        this.addCommand({
            id: 'clean-selected',
            name: 'Trims selected text and removes new line characters.',
            callback: function () { return _this.cleanSelected(); },
        });
        this.addCommand({
            id: 'insert-line-above',
            name: 'Insert line above current line',
            callback: function () { return _this.insertLine('above'); },
        });
        this.addCommand({
            id: 'insert-line-below',
            name: 'Insert line below current line',
            callback: function () { return _this.insertLine('below'); },
        });
        this.addCommand({
            id: 'clear-current-line',
            name: 'Clear current line',
            callback: function () { return _this.clearCurrentLine(); },
        });
        this.addCommand({
            id: 'toggle-readable-length',
            name: 'Toggle Readable Line Length',
            callback: function () {
                return _this.app.vault.setConfig('readableLineLength', !_this.app.vault.getConfig('readableLineLength'));
            },
        });
    };
    HotkeysPlus.prototype.clearCurrentLine = function () {
        var view = this.app.workspace.getActiveViewOfType(obsidian.MarkdownView);
        if (!view)
            return;
        var editor = view.editor;
        var lineNumber = editor.getCursor().line;
        editor.setLine(lineNumber, '');
    };
    HotkeysPlus.prototype.insertLine = function (mode) {
        var view = this.app.workspace.getActiveViewOfType(obsidian.MarkdownView);
        if (!view)
            return;
        var editor = view.editor;
        var lineNumber = editor.getCursor().line;
        var currentLineText = editor.getLine(lineNumber);
        var newLineText = '';
        if (currentLineText.trim().startsWith('- ')) {
            newLineText = currentLineText.substring(0, currentLineText.indexOf('- ') + 2);
        }
        for (var i = 1; i < 30; i++) {
            if (currentLineText.trim().startsWith(i.toString() + '. ')) {
                var correction = void 0;
                if (mode == 'above')
                    correction = -1;
                else
                    correction = 1;
                newLineText =
                    currentLineText.substring(0, currentLineText.indexOf(i.toString() + '. ')) +
                        (i + correction).toString() +
                        '. ';
            }
        }
        if (mode == 'above') {
            editor.replaceRange(newLineText + '\n', { line: lineNumber, ch: 0 });
            editor.setSelection({ line: lineNumber, ch: newLineText.length });
        }
        else {
            editor.replaceRange('\n' + newLineText, {
                line: lineNumber,
                ch: currentLineText.length,
            });
            editor.setSelection({ line: lineNumber + 1, ch: newLineText.length });
        }
    };
    HotkeysPlus.prototype.duplicateLines = function (mode) {
        var view = this.app.workspace.getActiveViewOfType(obsidian.MarkdownView);
        if (!view)
            return;
        var editor = view.editor;
        var selectedText = this.getSelectedText(editor);
        var newString = selectedText.content + '\n';
        if (mode === 'down') {
            editor.replaceRange(newString, selectedText.start, selectedText.start);
        }
        else {
            if (selectedText.end.line === editor.lastLine()) {
                // create a new line so that lastLine + 1 exists
                var newLastLineContent = editor.getLine(editor.lastLine()) + '\n';
                var cursorAnchor = editor.getCursor('anchor');
                var cursorHead = editor.getCursor('head');
                editor.setLine(editor.lastLine(), newLastLineContent);
                editor.setSelection(cursorAnchor, cursorHead); // preserve original cursor / selection state (adding a new line may have pushed the cursor down)
                newString = selectedText.content; // because there is no other content on the newly created line, we don't need a trailing newline char
            }
            var nextLineStart = {
                line: selectedText.end.line + 1,
                ch: 0,
            };
            editor.replaceRange(newString, nextLineStart, nextLineStart);
        }
    };
    HotkeysPlus.prototype.cleanSelected = function () {
        var view = this.app.workspace.getActiveViewOfType(obsidian.MarkdownView);
        if (!view)
            return;
        var editor = view.editor;
        var selectedText = this.getSelectedText(editor);
        var newString = selectedText.content.trim().replace(/(\r\n|\n|\r)/gm, ' ');
        newString = newString.replace(/  +/gm, ' ');
        editor.replaceRange(newString, selectedText.start, selectedText.end);
    };
    HotkeysPlus.prototype.onunload = function () {
        console.log('Unloading Hotkeys++ plugin');
    };
    HotkeysPlus.prototype.getSelectedText = function (editor) {
        if (editor.somethingSelected()) {
            // Toggle to-dos under the selection
            var cursorStart = editor.getCursor('from');
            var cursorEnd = editor.getCursor('to');
            var content = editor.getRange({ line: cursorStart.line, ch: 0 }, { line: cursorEnd.line, ch: editor.getLine(cursorEnd.line).length });
            return {
                start: { line: cursorStart.line, ch: 0 },
                end: {
                    line: cursorEnd.line,
                    ch: editor.getLine(cursorEnd.line).length,
                },
                content: content,
            };
        }
        else {
            // Toggle the todo in the line
            var lineNr = editor.getCursor().line;
            var contents = editor.getDoc().getLine(lineNr);
            var cursorStart = {
                line: lineNr,
                ch: 0,
            };
            var cursorEnd = {
                line: lineNr,
                ch: contents.length,
            };
            var content = editor.getRange(cursorStart, cursorEnd);
            return { start: cursorStart, end: cursorEnd, content: content };
        }
    };
    HotkeysPlus.prototype.toggleElement = function (re, subst) {
        var view = this.app.workspace.getActiveViewOfType(obsidian.MarkdownView);
        if (!view)
            return;
        var editor = view.editor;
        var selection = editor.somethingSelected();
        var selectedText = this.getSelectedText(editor);
        var newString = selectedText.content.replace(re, subst);
        editor.replaceRange(newString, selectedText.start, selectedText.end);
        // Keep cursor in the same place
        if (selection) {
            editor.setSelection(selectedText.start, {
                line: selectedText.end.line,
                ch: editor.getLine(selectedText.end.line).length,
            });
        }
    };
    HotkeysPlus.prototype.toggleTodos = function () {
        var re = /(^\s*|^\t*)(-\s\[ \]\s|-\s\[x\]\s|\*\s|-\s|\d*\.\s|\*\s|\b|^)([^\n\r]*)/gim;
        return this.toggleElement(re, this.replaceTodoElement);
    };
    HotkeysPlus.prototype.toggleLists = function () {
        var re = /(^\s*|^\t*)(-\s\[ \]\s|-\s\[x\]\s|\*\s|-\s|\d*\.\s|\*\s|\b|^)([^\n\r]*)/gim;
        return this.toggleElement(re, this.replaceListElement);
    };
    HotkeysPlus.prototype.toggleBlockQuote = function () {
        var re = />\s|^/gim;
        return this.toggleElement(re, this.replaceBlockQuote);
    };
    HotkeysPlus.prototype.toggleEmbed = function () {
        var re = /\S*\[\[/gim;
        return this.toggleElement(re, this.replaceEmbed);
    };
    HotkeysPlus.prototype.replaceListElement = function (match, spaces, startText, sentence) {
        if (startText === '- ') {
            return spaces + '1. ' + sentence;
        }
        else if (startText === '') {
            return spaces + '- ' + sentence;
        }
        else if (startText === '1. ') {
            return spaces + '' + sentence;
        }
        else {
            return spaces + '- ' + sentence;
        }
    };
    HotkeysPlus.prototype.replaceBlockQuote = function (startText) {
        if (startText === '> ') {
            return '';
        }
        else if (startText === '') {
            return '> ';
        }
        else {
            return '> ';
        }
    };
    HotkeysPlus.prototype.replaceEmbed = function (startText) {
        if (startText === '![[') {
            return '[[';
        }
        else if (startText === '[[') {
            return '![[';
        }
        else {
            return '';
        }
    };
    HotkeysPlus.prototype.replaceTodoElement = function (match, spaces, startText, sentence) {
        if (startText === '- [ ] ') {
            return spaces + '- [x] ' + sentence;
        }
        else if (startText === '- [x] ') {
            return spaces + '- ' + sentence;
        }
        else {
            return spaces + '- [ ] ' + sentence;
        }
    };
    return HotkeysPlus;
}(obsidian.Plugin));

module.exports = HotkeysPlus;


/* nosourcemap */