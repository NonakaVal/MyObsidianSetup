---
tags:
  - learning
  - oldVoult
HUB:
  - "[[hub-aoc]]"
---
### 5.3.1 Registrador de dados de memória (RDM) e de endereços de memória (REM)

O RDM (Registrador de Memória de Dados) ou MBR (Memory Buffer Register) é um registrador da UCP que armazena temporariamente dados que estão sendo transferidos da memória principal para a UCP ou da UCP para a memória principal. Ele permite que os dados sejam reencaminhados para outro elemento da UCP para processamento ou para uma célula da memória principal. A quantidade de bits que pode ser armazenada no RDM é determinada pela largura do barramento de dados.

O   Ele permite que a controladora de memória possa identificar e localizar a célula desejada. A quantidade de bits que pode ser armazenada no REM é a mesma quantidade suportada pelo barramento de endereço, que é responsável por transmitir o endereço da célula na memória que se deseja acessar..