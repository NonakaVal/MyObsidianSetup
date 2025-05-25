---
tags:
  - learning
  - tocomplete/atomizar
  - tocomplete/refatorar
HUB:
  - "[[System/HUB/hub-tec]]"
---
Principais modelos e plataformas para implementação da infraestrutura de ambientes de computação em nuvem

O modelo de implementação definem aspectos de controle de acesso, segurança e disponibilidade dos recursos computacionais ofertados como serviços 
Existem quatro modelos de implementação

Nuvem privada : Ambiente dedicado a uma única organização, é caraterizado pelo uso exclusivo dos recursos por uma organização que mantém uma infraestrutura onde os recursos são usados por diferentes setores de uma MESMA organização
Nuvem comunitária : Ambiente de computação em nuvem dedicado a um conjunto de organizações que compartilham recursos
Nuvem pública : ambiente de computação em nuvem mantido por um provedor que oferta serviços sob demanda para diversos clientes 
Nuvem híbrida : Modelo que envolve mais de um tipo de implementação

Plataforma de computação em nuvem : usada para realizar a gerência da infraestrutura 
Consiste no conjunto de ferramentas de software utilizados para gerenciar os servidores e equipamentos de redes que formam a infraestrutura, plataformas de computação também são conhecidos como software do servidor ou sistema operacional de nuvem, diversas plataformas de computação podem ser distribuídas como softwares livres, podendo ser usadas na implementação de modelos publicas ou privadas destacando as seguintes plataformas:
- OpenStack, CloudStack, Eucalyptus e OpenNebula

OpenStack : Combinação de ferramentas open source (projetos) que usam um pool de recursos virtuais para criar e gerenciar nuvens públicas e privadas
funciona como um sistema operacional para controlar recursos de processamento, armazenamento e rede.
criada a partir da colaboração da nasa e a empresa rackspace a partir de 2010
- Principais funcionalidades
	- Gerenciamento de maquinas virtuais 
	- Orquestração de contêineres
	- Balanceamento de carga 
	- Virtualização de funções de rede e controle de acesso aos recursos

Com uma arquitetura modular, a plataforma openstack combina diversos módulos funcionais 
seus projetos básicos são:
- Nova : Gerenciamento de instância computacionais (maquinas virtuais)
- Nêurtron : Gerenciamento de conectividade e virtualização de serviços de rede
- Switf : Armazenamento distribuído de alta disponibilidade para objetos e dados não estruturas como vídeos, backups, imagens
- Cinder: Gerenciamento de armazenamento em bloco (discos virtuais), por exemplo, para criar dispositivo lógico de armazenamento persistente para maquinas virtuais
- KeyStone: Gerenciamento de identidades, autenticação e controle de acesso
- Glance: gerenciamento de imagens de maquinas virtuais



