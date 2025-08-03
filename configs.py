#Lib com as constantes e configurações do projeto
#Libs
from configsCriaturas import CriaturaCFG

#Classes
#Globais
class Cores:
    """Subbiblioteca com as cores"""
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    RED = '\033[91m'      
    GREEN = '\033[92m'    
    BLUE = '\033[94m'     
    PURPLE = '\033[95m'


class Dados:
    """Subblioteca com os tipos de dados do projeto."""

    D2 = 2
    D4 = 4
    D6 = 6
    D8 = 8
    D10 = 10
    D12 = 12
    D20 = 20


class Combate:
    """Guarda alguns valores especificos e importantes para combate."""
    
    #Rolagens
    ROLAGEM_PADRAO: int = Dados.D6
    DANO_FALHA = 0
    FALHA = 1
    CRITICO = 6

    #Critico
    RESTAURACAO_MANA_CRITICO = 1
    MULTIPLICADOR_CRITICO_PADRAO = 2
    
    #Delays
    DELAY_CURTO: int = 1
    DELAY_MEDIO: int = 3
    DELAY_LONGO: int = 5


#Jogadores
class PALADINO():
    """Configurações básicas paladino"""
    CFG_STATUS: CriaturaCFG = CriaturaCFG()
    CFG_STATUS.NOME = 'paladino'
    CFG_STATUS.VIDA = 80
    CFG_STATUS.MANA = 0
    CFG_STATUS.MULTIPLICADOR_CRITICO = 2


    ID_ATAQUE_BASICO: int = 1
    DANO_ATAQUE_BASICO: int = 10
    RESTAURACAO_MANA_CRITICO: int = 1


    ID_ATAQUE_ESPECIAL: int = 3
    DANO_ATAQUE_ESPECIAL: int = 25
    CUSTO_ATAQUE_ESPECIAL: int = 5
    

    ID_RECUPERAR_FOLEGO: int = 1
    TIPO_DADO_RECUPERAR_FOLEGO: int = Dados.D10
    QUANTIDADE_DADOS_RECUPERAR_FOLEGO: int = 2
    RESTAURACAO_MANA_RECUPERAR_FOLEGO: int = 1


class ASSASSINO(): 
    """Configurações da classe de Assassino"""

    NOME: str = 'Assassino'
    VIDA: int = 50
    MANA: int = 0
    MULTIPLICADOR_CRITICO: int = Combate.MULTIPLICADOR_CRITICO_PADRAO


    ID_ATAQUE_BASICO: int = 1
    DANO_ATAQUE_BASICO: int = 12
    CURA_ATAQUE_BASICO: int = 4
    ATAQUE_BASICO_EFEITO: str = 'cura'
    ID_ATAQUE_AREA: int = 2
    DANO_ATAQUE_AREA: int = 6
    CURA_ATAQUE_AREA: int = 2
    
    ID_ATAQUE_ESPECIAL: int = 3
    DANO_ATAQUE_ESPECIAL: int = 28
    CUSTO_ATAQUE_ESPECIAL: int = 4
    

class CLERIGO():
    """Configurações básicas do clérigo"""

    #Status Base
    NOME: str = 'Clérigo'
    VIDA: int = 100
    MANA_MAXIMA: int = 10
    MANA_INICIAL: int = 5
    MULTIPLICADOR_CRITICO: int = Combate.MULTIPLICADOR_CRITICO_PADRAO
    RESTAURACAO_MANA_CRITICO: int = 1

    #Bola de Fogo
    ID_BOLA_FOGO: int = 1
    DANO_BOLA_FOGO: int = 5
    EFEITO_BOLA_FOGO: str = 'queimadura'
    CUSTO_BOLA_FOGO: int = 1

    #Meditação
    ID_MEDITACAO: int = 1
    RECUPERACAO_MANA_MEDITACAO: int = 3

    #Magia Cura
    ID_MAGIA_CURA: int = 2
    CURA_MAGIA_CURA: int = 5


#Inimigos
class ESQUELETO():
    """Configurações da classe Esqueleto."""

    NOME: str = 'esqueleto'
    VIDA: int = 10
    MANA: int = 0
    MULTIPLICADOR_CRITICO: int = Combate.MULTIPLICADOR_CRITICO_PADRAO

    ID_ATAQUE_BASICO: int = 1
    DANO_ATAQUE_BASICO: int = 4


class LICH():
    """Configuroções da classe de Lich."""

    NOME: str = 'Lich'
    VIDA: int = 100
    MANA: int = 0
    MULTIPLICADOR_CRITICO: int = Combate.MULTIPLICADOR_CRITICO_PADRAO

    ID_ATAQUE_BASICO: int = 1
    DANO_ATAQUE_BASICO: int = 10

    ID_INVOCAR_ESQUELETO: int = 2
    QUANTIDADE_ESQUELETOS_INVOCADOS: int = 1


class Menus:
    """Constantes de configurações de menus."""

    MENU_ATAQUE = 1
    MENU_BUFFS = 2