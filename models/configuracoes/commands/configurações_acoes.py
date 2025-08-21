#Configurações para commands de ações das criaturas.
#libs


#Classes
class ConfiguracaoBasicaAtaque:
    """Classe abstrata para configs basicas de ataque."""
    def __init__(self) -> None:
        #Infos Necessárias
        self.ID: int
        self.DANO: int
        self.CUSTO: int
        self.TIPO_CUSTO: str
        self.MULTIPLICADOR_CRITICO: int
        self.MENSAGENS: MensagensRolagem = MensagensRolagem()


class ConfiguracaoInvocacao:
    def __init__(self) -> None:
        self.ID: int
        self.CRIATURA: Criatura
        self.QUANTIDADE_INVOCACOES: int
        self.QUANTIDADE_INVOCACOES_CRITICO: int
        self.MENSAGENS = MensagensRolagem()


class RecuperarStatusDado:
    def __init__(self) -> None:
        self.ID: int = -1
        self.TIPO_DADO: int = -1
        self.QUANTIDADE_DADOS: int = -1
        self.STATUS_RECUPERADO: str = ''


class RecuperarStatus:
    ID: int
    QUANTIDADE: int
    STATUS_RECUPERADO: str


#Classes Especificas
class RecuperarFolego:
    ID: int
    VIDA: RecuperarStatusDado = RecuperarStatusDado()
    MANA: RecuperarStatus = RecuperarStatus()
    MENSAGENS = MensagensRolagem()
