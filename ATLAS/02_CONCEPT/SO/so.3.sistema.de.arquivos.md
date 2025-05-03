---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-SistemaOperacional]]"
---
---

![[2.59-arquivo-atribuicao-de-nomes,-estrutura,-tipos,-acesso,-atributos-e-operacoes]]

![[2.60-operacoes-sistemas-de-arquivo]]

![[2.61-tipo-logico-ou-fisico]]

Vejamos o exemplo em que são apresentadas as organizações de arquivos do tipo sequencial e indexada: 

![[2.62-sequencial-(nao-estruturada)]]

![[2.63-indexada]]



![[2.64-relativa-ou-direta]]



![[2.65-organizacao-de-arquivos]]

![[2.66-diretorios-simples,-sistemas-de-diretorio-hierarquico,-nomes-de-caminho-e-operacoes]]

Confira, no exemplo a seguir, como acontece a localização de arquivos em estruturas de diretórios de nível único e com dois níveis:


![[2.67-estrutura-de-diretorios-de-nivel-unico]]


![[2.68-diretorio-com-dois-niveis]]

A estrutura de diretórios é como o sistema organiza logicamente os diversos arquivos contidos em um disco. O diretório é uma estrutura de dados que contém entradas associadas aos arquivos em que cada entrada armazena informações com localização física, nome, organização e demais atributos

Além dessas estruturas, temos ainda a de árvore, mapa de bits, lista encadeada e tabela de blocos livres. Observe as respectivas ilustrações:

![[2.69-na-estrutura-em-arvore,]]


![[2.70-mapa-de-bits]]

# lista encadeada

Uma forma alternativa de alocar informações em blocos de memória é por meio de listas encadeadas, que usam os blocos livres do disco para manter o controle. Cada bloco possui uma área que indica o endereço do próximo bloco disponível para armazenamento. Ao encontrar o primeiro bloco livre, ele aponta para o próximo bloco livre e assim sucessivamente, criando uma lista encadeada.


#### bloco livres

Outra forma comumente utilizada para alocação e gerência de espaço livre em memória é a tabela de blocos livres, que são alocados e também liberados de forma simultânea e, com isso, é possível visualizar apenas os espaços que realmente estão liberados no disco. Observe a ilustração:


Quando se fala de gerenciamento de alocação de espaço em disco, podemos mencionar algumas formas de se realizar essa tarefa. Vamos conhecer a alocação contígua, alocação encadeada e a alocação indexada



A alocação contígua ou sequencial, como estudado na seção anterior, refere-se ao armazenamento do arquivo em blocos. Ele pode ser baseado no conceito de fila, nesse caso chamado de first-fit, que significa que o primeiro espaço livre no disco será também o primeiro a ser alocado se o seu tamanho for compatível com a do arquivo; outro modo de realizar a alocação contígua é chamado best-fit, em que há a alocação do menor espaço livre para um arquivo que seja compatível com esse pequeno segmento de memória que esteja livre e, por fim, o mecanismo de alocação contígua, conhecido como work-fit. Nesse último, será alocado no espaço correspondente em disco o maior arquivo, no entanto, como não há uma ordenação por tamanho, é necessário buscar esse espaço por toda a lista antes da alocação

#### alocação encadeada

A alocação encadeada organiza os blocos de disco de acordo com o ponteiro que indica o próximo bloco livre. Isso permite que o arquivo seja dividido em várias partes, chamadas de fragmentos, alocados de acordo com o espaço disponível no HD. No entanto, a fragmentação pode aumentar o tempo de acesso e gravação do arquivo. Para melhorar a performance, é recomendada a desfragmentação do disco. 
Já na alocação indexada, é possível acessar diretamente o bloco de arquivos por meio de um índice estabelecido previamente. Isso agiliza as operações de leitura e gravação dos dados. O método utilizado é conhecido como acesso indexado ou acesso por chave. Esses conceitos são importantes para entender situações que podem ocorrer no mercado de trabalho ao lidar com sistemas operacionais e aplicações.

157
## Introdução à implementação do sistema de arquivos. Virtualização do sistema de arquivos e registro


Descritor de arquivos: “é um registro no qual são mantidas as informações a respeito do arquivo. Essas informações incluem os seus atributos, além de outros dados que não são visíveis aos usuários mas que são necessários para que o sistema operacional implemente as operações sobre arquivos” (OLIVEIRA; CARISSIMI; TOSCANI, 2010, p. 214).


O descritor de arquivos tem por função guardar as informações ou atributos dos arquivos. Ele possui as seguintes informações de acordo com os autores Oliveira, Carissimi e Toscani (2010, p. 214): 

• nome do arquivo; 
• sua extensão; 
• tamanho, sempre definido em bytes; 
• data e hora do último acesso; 
• data e hora da última alteração; 
• identificação do usuário que criou o arquivo; 
• lista de usuários com permissões e tipos de acessos;
• localização dos arquivos.

O conteúdo do arquivo, em caso de interrupções, permanecerá intacto e, consequentemente, o do descritor de arquivos também, sendo que o ideal é manter o descritor na mesma partição em que se encontra o arquivo. Isso facilita o acesso a ele. Lembre-se de que o descritor é acessado em todas as operações de leitura e escrita do arquivo.

Para tornar mais rápido o acesso aos arquivos, o sistema de arquivos mantém na memória uma tabela contendo todos os descritores dos arquivos em uso. Quando um arquivo entra em uso, o seu descritor é copiado do disco para a memória. Ele pode ser acessado rapidamente sempre que necessário

Uma das funções do sistema operacional, para controlar os arquivos que estão em uso e aqueles que já não estão mais, é disponibilizar a informação correta. Por exemplo, se o descritor teve o seu valor alterado, o sistema operacional salvará uma cópia que sobrepõe a anterior e, portanto, essa cópia em disco estará sempre atualizada. As chamadas de sistema open/close também são incumbidas da tarefa de verificar se o arquivo foi alterado, se está em uso ou não mais. Para que isso aconteça, é preciso que um parâmetro de leitura seja executado ou mesmo de escrita, respectivamente, como apresentado a seguir:

Uma tabela de descritores de arquivos abertos, também chamada de TDAA, é responsável por manter atualizadas as informações dos arquivos abertos. Isso ocorre para todos os processos do sistema, em função de um arquivo ser acessado por vários processos ao mesmo tempo

Nesse contexto, quando há uma chamada de sistema do tipo open, o sistema de arquivos trata essas informações com as seguintes ações:

164
180
