---
created: "[[2025-05-13]]"
tags:
  - doc
HUB:
  - "[[hub-pkm]]"
repo: https://github.com/mProjectsCode/obsidian-meta-bind-plugin
select: 3
---

# Input Values

## Selection Controls

### Dropdown Select

```meta-bind
INPUT[select(
  option(1, option 1), 
  option(2, option 2), 
  option(3, option 3), 
  showcase
):select]
```

```meta-bind
INPUT[select(
  option(1, option 1), 
  option(false, option 2), 
  option(null, option 3), 
  showcase
):select2]
```

```meta-bind
INPUT[select(
  option(1, option 1), 
  option(2, option 2), 
  option(3, option 3), 
  option(3, option 3), 
  option(2, option 2), 
  showcase
):select3]
```

### Multi-Select
```meta-bind
INPUT[multiSelect(
  option(option 1), 
  option(option 2), 
  option(option 3), 
  option(option 3), 
  option(option 2), 
  showcase
):multiSelect2]
```

```meta-bind
INPUT[multiSelect(
  option(1, option 1), 
  option(false, option 2), 
  option(null, option 3), 
  showcase
):multiSelect3]
```

### Inline Select
```meta-bind
INPUT[inlineSelect(option(a), option(b), showcase):select]
```

```meta-bind
INPUT[inlineSelect(option(1, a), option(2, b), showcase):select2]
```

```meta-bind
INPUT[inlineSelect(option(1 hour, a), option(2 hours, b), showcase):select3]
```

```meta-bind
INPUT[inlineSelect(option(null, nothing), option(foo, something), showcase):select4]
```

## List Controls

### List Suggester
```meta-bind
INPUT[listSuggester(optionQuery(#example-note), showcase):list2]
```
`VIEW[{list2}][link]`

```meta-bind
INPUT[listSuggester(optionQuery(#example-note), useLinks(false), showcase):list3]
```
`VIEW[{list3}][link]`

### Inline List
Some text: `INPUT[inlineList:list5]` some more text

### Inline List Suggester
```meta-bind
INPUT[inlineListSuggester(optionQuery(#example-note), option(something, other), useLinks(false), showcase):list4]
```
Some text: `INPUT[inlineListSuggester(optionQuery(#example-note), option(something, other), useLinks(false)):list4]` some more text

`INPUT[inlineListSuggester(optionQuery(#example-note), option(something, other), allowOther):list5]`

### Null Values
```meta-bind
INPUT[list(showcase):list6]
```

```meta-bind
INPUT[list(showcase):list]
```
`VIEW[{list}][link]`

```meta-bind
INPUT[list(showcase, multiLine):list]
```

## Date & Time Controls

### Date Selection
```meta-bind
INPUT[date(showcase):date1]
```

### Date Picker
```meta-bind
INPUT[datePicker(showcase):date2]
```

```meta-bind
INPUT[datePicker(showcase, defaultValue(null)):date3]
```

### Time Selection
```meta-bind
INPUT[time(showcase):time]
```

### DateTime Selection
```meta-bind
INPUT[dateTime(showcase):dateTime]
```

## Text Inputs

### Text Editor
```meta-bind
INPUT[editor(showcase):editor]
```

```meta-bind
INPUT[editor(showcase):editor2]
```

### Text Input
```meta-bind
INPUT[text(showcase):text]
```

```meta-bind
INPUT[text(showcase, limit(10)):text]
```

### Text Area
```meta-bind
INPUT[textArea(showcase, class(meta-bind-full-width), class(meta-bind-high)):textArea]
```

## Media Inputs

### Image Suggester
```meta-bind
INPUT[imageSuggester(optionQuery("Other/Images"), showcase):image]
```

## Numeric Inputs

### Number Input
```meta-bind
INPUT[number(showcase):number]
```

```meta-bind
INPUT[number(showcase):number2]
```

```meta-bind
INPUT[number(showcase, placeholder(test), defaultValue(-1)):number3]
```

```meta-bind
INPUT[number(showcase, placeholder(test), defaultValue(null)):number4]
```

### Progress Bar
```meta-bind
INPUT[progressBar(showcase, minValue(-10), maxValue(3)):progress1]
```

```meta-bind
INPUT[progressBar(showcase, minValue(0), maxValue(1), stepSize(0.1)):progress2]
```

```meta-bind
INPUT[progressBar(showcase, minValue(0), maxValue(10), stepSize(-1)):progress3]
```

```meta-bind
INPUT[progressBar(showcase, minValue(0), maxValue(10), stepSize(0.1)):progress4]
```

The labels can be hidden if they are not required:
```meta-bind
INPUT[progressBar(defaultValue(53), addLabels(false)):progress5]
```

With some css-snippets we can change the color of the progress bar:
```meta-bind
INPUT[progressBar(defaultValue(53), class(red-progress-bar)):progress6]
```

### Slider Controls
#### Simple Slider
```meta-bind
INPUT[slider(showcase):slider1]
```

#### Slider with Labels
```meta-bind
INPUT[slider(addLabels, showcase):slider1]
```

#### Slider with Custom Range
```meta-bind
INPUT[slider(addLabels, minValue(-20), maxValue(20), showcase):slider2]
```

```meta-bind
INPUT[slider(addLabels, minValue(0), maxValue(1000), showcase):slider3]
```

#### Slider with Custom Step Size
```meta-bind
INPUT[slider(addLabels, minValue(0), maxValue(10), stepSize(0.1), showcase):slider4]
```

## Suggester Controls

### Simple Suggester
```meta-bind
INPUT[suggester(
  option(option 1),
  option(option 2),
  option(option 3),
  showcase
):suggest]
```

```meta-bind
INPUT[suggester(
  option(option 1),
  option(option 2),
  option(option 3),
  allowOther,
  showcase
):suggest]
```

### Suggester with Dataview
Note: This will error if Dataview is not enabled.

`INPUT[suggester(optionQuery(#example-note)):fileSuggest]`

```meta-bind
INPUT[suggester(optionQuery(#example-note), showcase):fileSuggest]
```

```meta-bind
INPUT[suggester(optionQuery(#example-note), useLinks(partial), showcase):fileSuggest2]
```

```meta-bind
INPUT[suggester(optionQuery(#example-note), useLinks(false), showcase):fileSuggest3]
```

## Toggle Control
```meta-bind
INPUT[toggle(showcase):toggle1]
```

```meta-bind
INPUT[toggle(showcase, onValue(1), offValue(0), defaultValue(1)):toggle2]
```

# Buttons 

## Basic Button Syntax

### Inline Buttons
```
text `BUTTON[docs-button]` text
text `BUTTON[docs-button, docs, open-button]` text
```

### Block Buttons
```meta-bind
BUTTON[docs-button]
```

## Button Styles & Appearance
```meta-bind-button
style: primary
label: Open Meta Bind Playground
class: green-button
action:
  type: command
  command: obsidian-meta-bind-plugin:open-playground
```

Available styles: `primary`, `default`, `destructive`

## Button Actions

### Command Execution
```meta-bind-button
style: default
label: Run Command
action:
  type: command
  command: some-command-id
```

### Templater Integration
```meta-bind-button
style: default
label: "Run Templater File"
actions:
  - type: runTemplaterFile
    templateFile: "templates/templater/Say Hello Command.md"
```

### JavaScript Execution
```meta-bind-button
style: default
label: Run Custom JS
action:
  type: js
  file: testJsFile.js
  args: 
    greeting: "Meta Bind User"
```

### Opening Links
```meta-bind-button
style: primary
label: Open Internal Link
action:
  type: open
  link: "[[View Fields/Other Note|Other Note]]"
```

```meta-bind-button
style: primary
label: Open External Link
action:
  type: open
  link: https://www.example.com
```

### Theme Switching
```meta-bind-button
label: Switch to Light Mode
style: destructive
actions:
  - type: command
    command: theme:use-light
```

```meta-bind-button
label: Switch to Dark Mode
style: primary
actions:
  - type: command
    command: theme:use-dark
```

## Advanced Button Features

### Multiple Actions
```meta-bind-button
label: Multi-Action Button
style: primary
actions:
  - type: command
    command: workspace:new-tab
  - type: js
    file: "testJsFile.js"
```

### Special Action Types
```meta-bind-button
label: Input Action
actions:
  - type: command
    command: command-palette:open
  - type: input
    str: help
```

```meta-bind-button
label: Delayed Action
actions:
  - type: command
    command: switcher:open
  - type: sleep
    ms: 500
  - type: input
    str: PF2e
```

## Note Manipulation

### Modifying Frontmatter
```meta-bind-button
label: "+1"
style: default
actions:
  - type: updateMetadata
    bindTarget: count
    evaluate: true
    value: Math.min(10, x + 1)
```

### Content Replacement
```meta-bind-button
label: Replace Content
style: default
action:
  type: "replaceInNote"
  fromLine: 3
  toLine: 5
  replacement: "new content"
```

### Content Insertion
```meta-bind-button
label: Insert Text
style: default
action:
  type: "insertIntoNote"
  line: 38
  value: "inserted text"
```

### Self-Modifying Buttons
```meta-bind-button
label: Replace Self
style: default
action:
  type: "replaceSelf"
  replacement: "new content"
```

## Navigation Buttons

```meta-bind-button
label: Scroll to Section
style: default
actions:
  - type: open
    link: "[[#Section Name]]"
```

## Button Templates & Reusability

### Referencing Buttons
```
`BUTTON[button-id]`
`BUTTON[button1-id, button2-id]`
```

### Template Example
```meta-bind-button
label: Template Button
id: template-button
style: default
actions: []
```

## Error Handling

### Invalid Button Examples
```meta-bind-button
label: Invalid Button
actions:
  - type: sleep  # Missing ms parameter
  - type: invalid-type
```

Last modified : `$= dv.current().file.mtime`