---
tags:
  - learning
HUB:
  - "[[System/HUB/hub-tec]]"
---
[w3schools](https://www.w3schools.com/html/html_attributes.asp):luc_link:

###### Resumo do capítulo

-   Todos os elementos HTML podem ter atributos
-   O `href`atributo de `<a>`especifica a URL da página para a qual o link vai
-   O `src`atributo de `<img>`especifica o caminho para a imagem a ser exibida
-   Os atributos `width`e fornecem informações de tamanho para imagens`height``<img>`
-   O `alt`atributo de `<img>`fornece um texto alternativo para uma imagem
-   O `style`atributo é usado para adicionar estilos a um elemento, como cor, fonte, tamanho e mais
-   O `lang`atributo da `<html>`tag declara o idioma da página da Web
-   O `title`atributo define alguma informação extra sobre um elemento

-----

Os atributos HTML fornecem informações adicionais sobre os elementos HTML.

###### Atributos HTML

Todos os elementos HTML podem ter **atributos**
Os atributos fornecem **informações adicionais** sobre os elementos
Os atributos são sempre especificados na **tag de início**
Os atributos geralmente vêm em pares de nome/valor como: **name="value"**

##### O atributo href = link|hiperlink

A `<a>`tag define um hiperlink. O `href`atributo especifica a URL da página para a qual o link vai:

<*a href="https://www.w3schools.com">Visit W3Schools</a>


##### O Atributo src = imagem

A `<img>`tag é usada para incorporar uma imagem em uma página HTML. O `src`atributo especifica o caminho para a imagem a ser exibida:

<*img src="img_girl.jpg">

Há duas maneiras de especificar a URL no `src` atributo:

1. URL absoluta - Links para uma imagem externa que está hospedada em outro site. Exemplo: src="https://www.w3schools.com/images/img_girl.jpg" .

Observações: As imagens externas podem estar sob direitos autorais. Se você não obtiver permissão para usá-lo, poderá estar violando as leis de direitos autorais. Além disso, você não pode controlar as imagens externas; ele pode ser removido ou alterado repentinamente.

2. URL relativo - Links para uma imagem hospedada no site. Aqui, a URL não inclui o nome de domínio. Se a URL começar sem uma barra, ela será relativa à página atual. Exemplo: src="img_girl.jpg". Se a URL começar com uma barra, ela será relativa ao domínio. Exemplo: src="/images/img_girl.jpg".

**Dica:** quase sempre é melhor usar URLs relativos. Eles não vão quebrar se você mudar de domínio.


###### O Atributo Alt =  msg erro

O atributo obrigatório `alt`para a `<img>` tag especifica um texto alternativo para uma imagem, se a imagem por algum motivo não puder ser exibida. Isso pode ocorrer devido a uma conexão lenta ou a um erro no `src`atributo ou se o usuário usar um leitor de tela.

<*img src="img_girl.jpg" alt="Girl with a jacket">

