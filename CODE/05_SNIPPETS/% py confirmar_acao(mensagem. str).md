def confirmar_acao(mensagem: str) -> bool:
    """Solicita confirmação do usuário para uma ação."""
    resposta = input(f"{mensagem} (digite 'confirmar' para prosseguir): ").strip().lower()
    return resposta == "confirmar"