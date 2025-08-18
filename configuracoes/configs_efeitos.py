#Biblioteca de classes abstratas para efeitos
#libs
from .configs_criaturas import MensagensRolagem

#Classes abstratas
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