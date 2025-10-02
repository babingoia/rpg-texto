#Lib com as constantes e configurações do projeto
#Libs


#Classes
#Globais
class Dados:
    """Subblioteca com os tipos de dados do projeto."""

    D2 = 2
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20
    

class ConfigFactoryCriarCriaturas:
    def __init__(self) -> None:
        self.ESQUELETO: str = 'esqueleto'
        self.LICH: str = 'lich'
        self.PALADINO: str = 'paladino'
        self.ASSASSINO: str = 'assassino'
        self.CLERIGO: str = 'clerigo'


class Combate:
    """Guarda alguns valores especificos e importantes para combate."""
    
    #Rolagens
    ROLAGEM_PADRAO: int = Dados.D6
    DANO_FALHA: int = 0
    FALHA = 1
    CRITICO = 6

    #Critico
    RESTAURACAO_MANA_CRITICO = 1
    MULTIPLICADOR_CRITICO_PADRAO = 2
    
    #Delays
    DELAY_CURTO: int = 1
    DELAY_MEDIO: int = 3
    DELAY_LONGO: int = 5
