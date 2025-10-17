def list_files(path):
    """
    📂 Lista arquivos de um diretório
    
    Args:
        path (str): Caminho do diretório
    
    Returns:
        list[str]: Lista com os nomes dos arquivos (não inclui pastas)
    """
    try:
        return [
            f for f in os.listdir(path)
            if os.path.isfile(os.path.join(path, f))
        ]
    except (FileNotFoundError, PermissionError) as e:
        print(f"⚠️ Erro ao acessar '{path}': {e}")
    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")
    return []
