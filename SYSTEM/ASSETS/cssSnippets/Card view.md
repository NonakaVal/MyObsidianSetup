---
tags:
  - cssSnippetCollection 
HUB:
  - "[[hub-css]]"
---
# Card view

---

- author:: raisabelatrix
- source:: https://gist.github.com/raisabelatrix/a92a2c9c43c2deb2ebb5175f11631608

---

cover:: ![](https://i.imgur.com/YN56k3S.png)

```css
.card-view {
    --card-width:35em; /*adjust this size if you want narrower or wider cards*/
    /*unit has to be in em so that card background will scale along with your font
    when you zoom in and out*/
}

/*The Card*/
.card-view .markdown-preview-section {
    background-color: var(--background-primary);
    margin: 3% auto;
    max-width:var(--card-width)!important;
    padding: 3em!important;
    box-shadow: 7px 7px 5px 0px var(--background-modifier-box-shadow);

}

/*Card background*/
.markdown-reading-view .card-view {
    background-color: var(--background-secondary); /*dark bg in 1 pane*/
    padding-bottom: 350px;
}

/*Card title*/
.card-view h1 {
    font-size: 1.3em;
    color:inherit;
    margin-bottom:1em;
}

.markdown-reading-view .card-view h1 .heading-collapse-indicator {
    display: none;
}

/*Disable card view for embeds*/
.markdown-embed .card-view{
    min-height: 0!important;
    box-shadow: unset!important;
    background-color: unset!important;
}

.markdown-embed .card-view .markdown-preview-section {
    box-shadow: unset!important;
    padding: 0!important;
}

/*uncomment this line if you're using primary theme
.full-height-embeds .card-view .markdown-preview-sizer.markdown-preview-section {
    padding-bottom: 3em!important;
}*/
```
