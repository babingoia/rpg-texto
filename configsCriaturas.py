class CriaturaCFG:
    """Classe abstrata para configs basicas de criaturas."""
    NOME:str
    VIDA: int
    MANA: int
    MULTIPLICADOR_CRITICO: int

    #Ataque básico
    ID_ATAQUE_BASICO: int
    DANO_ATAQUE_BASICO: int
    RESTAURACAO_MANA_CRITICO: int

    MENSAGEM_INICIO: str
    MENSAGEM_FALHA: str
    MENSAGEM_NORMAL: str
    MENSAGEM_CRITICO: str