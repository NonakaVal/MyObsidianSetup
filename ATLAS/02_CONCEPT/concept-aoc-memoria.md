---
tags:
  - learning
  - 
HUB:
  - "[[hub-aoc]]"
---
# Subsistema de Memória

Componente fundamental para armazenamento de dados temporários ou permanentes, tão crucial quanto a UCP. Composto por diversos tipos de memórias interligadas com características distintas de:

- **Velocidade** (de registradores até memória secundária)
- **Capacidade** (inversamente proporcional à velocidade)
- **Custo** (por bit armazenado)

## Hierarquia de Memória

### ![[concept-aoc-memoria-1. Registradores|1. Registradores]]
- Memória mais rápida do sistema
- Localizados dentro da própria UCP
- Tamanho mínimo (tipicamente 32-64 bits por registrador)

### ![[concept-aoc-memoria-2. Memória Cache|2. Memória Cache]]
- Níveis: L1 (mais rápido), L2, L3 (maior)
- Taxa de acerto (hit rate) crítica para desempenho
- Políticas de substituição (LRU, FIFO)

### ![[concept-aoc-memoria-3. Memória Principal (RAM)|3. Memória Principal (RAM)]]
- Tipos: DRAM (dinâmica), SRAM (estática)
- Organização em bancos e canais
- Tempos de acesso: CAS Latency, RAS-to-CAS

### ![[concept-aoc-memoria-4. Memória ROM|4. Memória ROM]]
- Firmware e microcódigo
- Tecnologias: PROM, EPROM, EEPROM, Flash
- Não-volátil mas de leitura prioritária

### ![[concept-aoc-memoria-5. Memória Secundária|5. Memória Secundária]]
- Hierarquia de armazenamento permanente
- Meios magnéticos (HDD) vs sólidos (SSD)
- Trade-off custo/capacidade/desempenho