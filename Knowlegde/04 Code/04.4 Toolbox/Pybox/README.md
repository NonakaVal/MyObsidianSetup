# PyBox

Meus Scripts Python com diversos usos acumulado nesses anos de estudo centralizados para rodar por um comando no terminal debian, até atualizar esse repo eu usava de forma convencional abrindo/navegando/rodando, mas acho que já tenho códigos o bastante. por fim, adicionei globalmente o comando pybox que me permite escolher o que quero rodar organizado listas e módulos... 

## Estrutura

- `pybox.py`: menu principal para escolher módulos e scripts
- `config.py`: define os módulos e caminhos
- `modules/`: scripts agrupados em pastas como `audio`, `file_tools`, `gallery_tools`, `index_notes`, `manga_reader`, `obsidian_tools`, `shell_tools`

## Uso

1. Execute `python3 pybox.py`
2. Selecione um módulo
3. Escolha um script para rodar

## Ambiente

O `pybox.py` exporta variáveis de ambiente antes de executar cada script:

- `PYBOX_ROOT`
- `PYBOX_MODULES`
- `PYBOX_SCRIPT`
- `PYBOX_CALL_DIR`
