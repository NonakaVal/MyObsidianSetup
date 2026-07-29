---
share_link: https://share.note.sx/te9w3js0#gLh6CyCwidMFBAJzT6bB1Nu9yN79kuaDz0YRcrQXTeY
share_updated: 2026-03-24T17:21:49-03:00
subject:
  - "[[hub-SistemaOperacional]]"
  - "[[hub-tec]]"
---
# 🖥️ Aplicações Instaladas — ZorinOS
> Guia de comandos para iniciar e usar suas aplicações via terminal

---

## 🎬 Multimídia

### VLC — Player de Vídeo/Áudio
```bash
vlc
```
```bash
# Abrir um arquivo específico
vlc /caminho/para/video.mp4

# Abrir uma URL/stream
vlc https://exemplo.com/stream.m3u8

# Modo sem interface gráfica (headless)
vlc --intf rc video.mp4

# Converter vídeo para outro formato
vlc -I dummy entrada.mp4 --sout='#transcode{vcodec=h264}:std{access=file,dst=saida.mkv}' vlc://quit
```
**Usos principais:** reproduzir vídeos locais, streams online, playlists `.m3u`, converter mídias, transmissão em rede.

---

### OBS Studio — Gravação e Streaming
```bash
obs-studio
# ou simplesmente:
obs
```
```bash
# Iniciar em modo de estúdio
obs --startrecording

# Iniciar já em modo de streaming
obs --startstreaming
```
**Usos principais:** gravar a tela, fazer lives no YouTube/Twitch, capturar câmera, gravar tutoriais.

---

### Rhythmbox — Player de Música
```bash
rhythmbox
```
```bash
# Tocar/pausar pelo terminal
rhythmbox-client --play-pause

# Próxima música
rhythmbox-client --next

# Ajustar volume
rhythmbox-client --set-volume 0.8
```
**Usos principais:** ouvir músicas locais, organizar biblioteca, rádios online, podcasts.

---

### Totem — Player de Vídeo GNOME
```bash
totem
```
```bash
# Abrir arquivo diretamente
totem /caminho/para/video.mp4
```
**Usos principais:** reprodutor padrão do GNOME, integrado ao gerenciador de arquivos.

---

### Melt — Editor de Vídeo (linha de comando / MLT)
```bash
melt
```
```bash
# Reproduzir um vídeo
melt video.mp4

# Concatenar vídeos
melt video1.mp4 video2.mp4 -consumer avformat:saida.mp4

# Adicionar filtro de escala de cinza
melt video.mp4 -filter greyscale -consumer avformat:saida.mp4
```
**Usos principais:** edição de vídeo por linha de comando, base do Kdenlive, automação de processamento de vídeo.

---

### Mediainfo — Informações de Mídia
```bash
mediainfo arquivo.mp4
```
```bash
# Saída em formato texto
mediainfo --Output=TEXT video.mkv

# Saída em JSON
mediainfo --Output=JSON audio.flac

# Ver apenas informações de vídeo
mediainfo --Inform="Video;%Width%x%Height% | %FrameRate% fps" video.mp4
```
**Usos principais:** ver codec, resolução, bitrate, duração e metadados de qualquer arquivo de mídia.

---

## 🖥️ Escritório

### LibreOffice Writer — Editor de Texto
```bash
libreoffice --writer
```
```bash
# Abrir um arquivo .docx
libreoffice --writer documento.docx

# Converter .docx para PDF via terminal
libreoffice --headless --convert-to pdf documento.docx

# Converter pasta inteira de .odt para .pdf
libreoffice --headless --convert-to pdf *.odt
```
**Usos principais:** escrever documentos, editar .docx/.odt, exportar para PDF.

---

### LibreOffice Calc — Planilhas
```bash
libreoffice --calc
```
```bash
# Abrir um .xlsx
libreoffice --calc planilha.xlsx

# Converter para PDF
libreoffice --headless --convert-to pdf planilha.xlsx
```
**Usos principais:** criar e editar planilhas, cálculos, gráficos, compatível com Excel.

---

### LibreOffice Impress — Apresentações
```bash
libreoffice --impress
```
```bash
# Abrir um .pptx
libreoffice --impress apresentacao.pptx

# Converter apresentação para PDF
libreoffice --headless --convert-to pdf apresentacao.pptx

# Exportar slides como imagens PNG
libreoffice --headless --convert-to png apresentacao.pptx
```
**Usos principais:** criar slides, editar .pptx, exportar apresentações.

---

## 🌐 Internet e Rede

### Remmina — Acesso Remoto (RDP/VNC)
```bash
remmina
```
```bash
# Conectar via RDP diretamente
remmina -c rdp://usuario@192.168.1.100

# Conectar via VNC
remmina -c vnc://192.168.1.100

# Abrir um perfil salvo
remmina -c /caminho/para/perfil.remmina
```
**Usos principais:** acessar Windows remotamente via RDP, controlar outros Linux via VNC, suporte remoto.

---

### wget — Download de Arquivos
```bash
wget https://exemplo.com/arquivo.zip
```
```bash
# Baixar com nome personalizado
wget -O meu-arquivo.zip https://exemplo.com/arquivo.zip

# Retomar download interrompido
wget -c https://exemplo.com/arquivo-grande.iso

# Baixar site completo para uso offline
wget --mirror --convert-links https://exemplo.com

# Download em background
wget -b https://exemplo.com/arquivo.iso
```
**Usos principais:** baixar arquivos, ISOs, scripts, mirroring de sites.

---

### OpenSSH Client — Acesso SSH
```bash
ssh usuario@192.168.1.100
```
```bash
# Conectar em porta diferente
ssh -p 2222 usuario@servidor.com

# Copiar arquivo para servidor remoto
scp arquivo.txt usuario@servidor.com:/home/usuario/

# Copiar arquivo do servidor para local
scp usuario@servidor.com:/caminho/arquivo.txt ./

# Túnel SSH (porta local → remota)
ssh -L 8080:localhost:80 usuario@servidor.com
```
**Usos principais:** acessar servidores remotamente, copiar arquivos via rede, criar túneis seguros.

---

### OpenVPN — VPN
```bash
sudo openvpn --config minha-vpn.ovpn
```
```bash
# Rodar em background
sudo openvpn --config minha-vpn.ovpn --daemon

# Ver log de conexão
sudo openvpn --config minha-vpn.ovpn --log /tmp/vpn.log
```
**Usos principais:** conectar a VPNs corporativas ou pessoais, privacidade de rede.

---

### netcat — Ferramenta de Rede
```bash
nc
```
```bash
# Testar se uma porta está aberta
nc -zv 192.168.1.1 80

# Criar servidor de teste simples
nc -l 8080

# Transferir arquivo via rede (receptor)
nc -l 9999 > arquivo_recebido.txt

# Transferir arquivo via rede (emissor)
nc 192.168.1.50 9999 < arquivo.txt
```
**Usos principais:** testar portas, transferir arquivos em rede local, depurar conexões.

---

### tcpdump — Captura de Pacotes de Rede
```bash
sudo tcpdump
```
```bash
# Capturar tráfego de uma interface
sudo tcpdump -i eth0

# Filtrar por host
sudo tcpdump host 192.168.1.1

# Filtrar por porta
sudo tcpdump port 80

# Salvar captura em arquivo
sudo tcpdump -w captura.pcap

# Ler arquivo de captura salvo
tcpdump -r captura.pcap
```
**Usos principais:** analisar tráfego de rede, diagnosticar problemas, monitorar conexões.

---

### mtr — Traceroute Avançado
```bash
mtr google.com
```
```bash
# Modo não-interativo com relatório
mtr --report google.com

# Mostrar IPs em vez de hostnames
mtr -n 8.8.8.8

# Número de pings por host
mtr --report-cycles 20 google.com
```
**Usos principais:** diagnosticar latência de rede, encontrar onde os pacotes se perdem.

---

### rsync — Sincronização de Arquivos
```bash
rsync -av origem/ destino/
```
```bash
# Sincronizar para servidor remoto
rsync -avz /pasta/local/ usuario@servidor:/pasta/remota/

# Sincronizar apenas arquivos modificados
rsync -avzu origem/ destino/

# Simular sem executar (dry-run)
rsync -avn origem/ destino/

# Backup com exclusão de arquivos removidos
rsync -av --delete origem/ destino/
```
**Usos principais:** backup de arquivos, sincronização de pastas, cópia eficiente em rede.

---

### UFW — Firewall
```bash
sudo ufw status
```
```bash
# Ativar/desativar firewall
sudo ufw enable
sudo ufw disable

# Liberar porta SSH
sudo ufw allow ssh

# Liberar porta específica
sudo ufw allow 8080/tcp

# Bloquear IP
sudo ufw deny from 192.168.1.50

# Ver regras numeradas
sudo ufw status numbered
```
**Usos principais:** proteger o sistema com firewall simples, liberar/bloquear portas e IPs.

---

## 🍷 Windows no Linux

### Wine — Rodar Programas Windows
```bash
wine programa.exe
```
```bash
# Configurar Wine
winecfg

# Instalar programa Windows
wine setup.exe

# Rodar com versão específica do Windows simulada
WINEARCH=win32 wine programa.exe

# Ver processos Wine rodando
wine taskmgr
```
**Usos principais:** executar programas `.exe` do Windows sem precisar de VM.

---

### Winetricks — Facilitar instalações Wine
```bash
winetricks
```
```bash
# Instalar componentes necessários para jogos/apps
winetricks vcrun2019
winetricks dotnet48
winetricks d3dx9

# Interface gráfica
winetricks --gui
```
**Usos principais:** instalar bibliotecas do Windows (DirectX, .NET, Visual C++) para compatibilidade com Wine.

---

## 🖥️ Sistema e Utilitários

### nano — Editor de Texto no Terminal
```bash
nano arquivo.txt
```
```bash
# Editar arquivo de sistema (como root)
sudo nano /etc/hosts

# Abrir em modo somente leitura
nano -v arquivo.txt

# Abrir com número de linha
nano +20 arquivo.txt
```
**Usos principais:** editar arquivos de configuração, scripts, textos rápidos no terminal.

---

### vim — Editor de Texto Avançado
```bash
vim arquivo.txt
```
```bash
# Abrir e ir para linha específica
vim +50 arquivo.txt

# Modo somente leitura
vim -R arquivo.txt

# Comparar dois arquivos
vimdiff arquivo1.txt arquivo2.txt
```
**Usos principais:** edição avançada de código e configurações, altamente configurável.

---

### htop / sysstat — Monitoramento do Sistema
```bash
# Ver processos em tempo real
htop

# Estatísticas da CPU
mpstat

# Uso de I/O de disco
iostat

# Estatísticas de memória
vmstat
```
**Usos principais:** monitorar CPU, RAM, processos, disco em tempo real.

---

### lshw — Informações de Hardware
```bash
sudo lshw
```
```bash
# Mostrar apenas resumo
sudo lshw -short

# Informações da placa de vídeo
sudo lshw -C display

# Informações de rede
sudo lshw -C network

# Exportar para HTML
sudo lshw -html > hardware.html
```
**Usos principais:** ver detalhes completos do hardware do seu computador.

---

### lm-sensors — Temperatura e Sensores
```bash
sensors
```
```bash
# Detectar sensores disponíveis
sudo sensors-detect

# Ver temperaturas continuamente
watch -n 1 sensors
```
**Usos principais:** monitorar temperatura da CPU, GPU e outros sensores.

---

### lsof — Arquivos/Portas em Uso
```bash
lsof
```
```bash
# Ver quem está usando uma porta
sudo lsof -i :8080

# Arquivos abertos por um processo
lsof -p 1234

# Ver conexões de rede ativas
sudo lsof -i -n -P
```
**Usos principais:** descobrir qual processo está usando uma porta ou arquivo.

---

### strace — Depurar Programas
```bash
strace comando
```
```bash
# Rastrear chamadas de sistema de um processo
strace -p 1234

# Salvar rastreamento em arquivo
strace -o saida.log programa

# Ver apenas erros
strace -e trace=open programa 2>&1 | grep ENOENT
```
**Usos principais:** depurar falhas em programas, descobrir arquivos que um programa tenta acessar.

---

### tree — Visualizar Estrutura de Pastas
```bash
tree
```
```bash
# Limitar profundidade
tree -L 2

# Mostrar apenas diretórios
tree -d

# Incluir tamanho dos arquivos
tree -sh

# Exportar estrutura para texto
tree > estrutura.txt
```
**Usos principais:** visualizar estrutura de projetos, documentar organização de pastas.

---

### p7zip — Compressão de Arquivos
```bash
7z
```
```bash
# Compactar pasta
7z a arquivo.7z pasta/

# Extrair arquivo
7z x arquivo.7z

# Listar conteúdo sem extrair
7z l arquivo.7z

# Compactar com senha
7z a -p arquivo.7z pasta/

# Extrair para pasta específica
7z x arquivo.7z -o/destino/
```
**Usos principais:** compactar e extrair arquivos .7z, .zip, .rar, .tar e outros.

---

### zip / unzip — Arquivos ZIP
```bash
zip -r arquivo.zip pasta/
unzip arquivo.zip
```
```bash
# Compactar apenas arquivos .txt
zip textos.zip *.txt

# Extrair em pasta específica
unzip arquivo.zip -d /destino/

# Ver conteúdo sem extrair
unzip -l arquivo.zip

# Extrair arquivo específico do ZIP
unzip arquivo.zip arquivo-especifico.txt
```
**Usos principais:** criar e extrair arquivos .zip compatíveis com Windows e outros sistemas.

---

### rsyslog — Logs do Sistema
```bash
# Ver logs do sistema em tempo real
sudo tail -f /var/log/syslog

# Ver últimas 100 linhas
sudo tail -100 /var/log/syslog

# Buscar erros nos logs
sudo grep -i error /var/log/syslog
```
**Usos principais:** monitorar eventos do sistema, diagnosticar falhas e erros.

---

### NVIDIA Settings — Configurar GPU NVIDIA
```bash
nvidia-settings
```
```bash
# Ver informações da GPU
nvidia-smi

# Monitorar GPU em tempo real
watch -n 1 nvidia-smi

# Ver temperatura da GPU
nvidia-smi --query-gpu=temperature.gpu --format=csv
```
**Usos principais:** configurar resolução, múltiplos monitores, monitorar uso e temperatura da GPU NVIDIA.

---

### sshfs — Montar Pasta Remota via SSH
```bash
sshfs usuario@servidor:/pasta/remota /ponto/de/montagem/
```
```bash
# Montar servidor remoto
mkdir ~/servidor-remoto
sshfs usuario@192.168.1.100:/home/usuario ~/servidor-remoto

# Desmontar
fusermount -u ~/servidor-remoto

# Montar com porta customizada
sshfs -p 2222 usuario@servidor:/home ~/servidor-remoto
```
**Usos principais:** acessar arquivos de um servidor remoto como se fossem locais.

---

### nodejs — JavaScript no Terminal
```bash
node
```
```bash
# Executar script JavaScript
node script.js

# REPL interativo
node

# Verificar versão
node --version

# Executar com variáveis de ambiente
NODE_ENV=production node app.js
```
**Usos principais:** rodar scripts JavaScript, desenvolvimento web, automações.

---

### python3 — Python no Terminal
```bash
python3
```
```bash
# Executar script
python3 script.py

# Shell interativo
python3

# Instalar pacote
pip3 install requests

# Criar servidor HTTP simples
python3 -m http.server 8080

# Criar ambiente virtual
python3 -m venv meu-env
source meu-env/bin/activate
```
**Usos principais:** rodar scripts, automações, desenvolvimento, análise de dados.

---

### rustc — Compilador Rust
```bash
rustc main.rs
```
```bash
# Compilar e rodar
rustc main.rs && ./main

# Verificar versão
rustc --version

# Criar projeto com Cargo
cargo new meu-projeto
cd meu-projeto
cargo run
```
**Usos principais:** compilar programas em Rust, desenvolvimento de software de alto desempenho.

---

### make — Automatizar Compilação
```bash
make
```
```bash
# Executar target específico
make install
make clean
make build

# Ver targets disponíveis
make help

# Executar com múltiplos núcleos
make -j4
```
**Usos principais:** compilar projetos C/C++, executar tarefas automatizadas de build.

---

### ufw — Firewall Simplificado
```bash
sudo ufw status verbose
```
*(ver seção Internet e Rede acima)*

---

## 🔧 Manutenção do Sistema

### Atualizar sistema completo
```bash
sudo apt update && sudo apt upgrade -y
```

### Limpar pacotes desnecessários
```bash
sudo apt autoremove --purge -y
sudo apt autoclean
```

### Ver espaço em disco
```bash
df -h
du -sh ~/
```

### Verificar pacotes instalados
```bash
# APT
apt list --installed 2>/dev/null | grep -v "lib"

# Flatpak
flatpak list --app

# Snap
snap list
```

### Reinstalar um pacote
```bash
sudo apt install --reinstall nome-do-pacote
```

### Remover pacote completamente
```bash
sudo apt purge nome-do-pacote && sudo apt autoremove
```
