#Biblioteca de classes abstratas para efeitos
#libs


#Classes abstratas
class RecuperarStatusDado:
    ID: int
    TIPO_DADO: int
    QUANTIDADE_DADOS: int
    STATUS_RECUPERADO: str


class RecuperarStatus:
    ID: int
    QUANTIDADE: int
    STATUS_RECUPERADO: str


#Classes Especificas
class RecuperarFolego:
    ID: int
    VIDA: RecuperarStatusDado = RecuperarStatusDado()
    MANA: RecuperarStatus = RecuperarStatus()