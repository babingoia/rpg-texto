#Configurações abstratas das criaturas.
#Libs
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Criatura

#Classes Basicas
class MensagensRolagem:
    """Classe abstrata para mensagens de rolagens de dados."""
    def __init__(self) -> None:
        self.MENSAGEM_INICIO: str
        self.MENSAGEM_FALHA: str = "\nInfelizmente você erra o ataque."
        self.MENSAGEM_NORMAL: str
        self.MENSAGEM_CRITICO: str


class ConfiguracaoStatus:
    """Classe abstrata para configs basicas de criaturas."""
    def __init__(self) -> None:
        self.NOME:str
        self.VIDA: int


class ConfiguracaoMago:
    """Classe abstrata para configs especificas de magos."""
    def __init__(self) -> None:
        self.MANA_MAXIMA: int
        self.MANA_INICIAL: int = 0
        self.RESTAURACAO_MANA_CRITICO: int


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
