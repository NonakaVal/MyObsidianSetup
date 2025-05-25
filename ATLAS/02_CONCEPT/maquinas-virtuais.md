---
tags:
  - learning
created: "[[2024-03-18]]"
HUB:
  - "[[System/HUB/hub-tec]]"
---
### [[maquinas-virtuais]]

Chamamos de máquinas virtuais os ambientes de processamento criados nos hardware dos [[provedores]] , graças a [[virtualizacao|virtualizacao]] diversas máquinas virtuais podem ser criadas em um mesmo servidor, permitindo que os processos sejam isolados para garantir a segurança e privacidade da distribuição e uso dos recursos, sendo possível também o uso de diferentes sistemas operacionais em diferentes maquinas virtuais em um mesmo servidor.

Fatores fundamentais na [[virtualizacao|virtualizacao]] para a [[computacao-em-nuvem]]

- info Independência de hardware
	- O processo de virtualização reduz os problemas de compatibilidade, simplificando a migração das aplicações nesse sistema desde que o formato da máquina virtual seja suportado pelo [[hypervisor]].
- info Consolidação de servidores
	- Processo usado para gerenciar a eficiência no uso dos servidores em um centro de dados, para reduzir custos e economizar energia.
		- uma forma de consolidação de servidores é a migração de VMs para servidores com recursos disponíveis de forma que, quando possível, seja desligado servidores vazios.
- info Facilidade de reaplicação
	- A facilidade de reaplicação das [[concept-instancias-maquinas-virtual|instancias]]  de máquinas virtuais nos servidores físicos


- ~ representação de máquinas virtuais em um servidor físico.
![vm-machine-img-repre](https://i.imgur.com/5OImf5N.png)
