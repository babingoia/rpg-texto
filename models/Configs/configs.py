#Lib com as constantes e configurações do projeto
#Libs
from .configsCriaturas import ConfiguracaoMago, ConfiguracaoBasicaAtaque, ConfiguracaoStatus
from .configsEfeitos import RecuperarFolego


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


#Jogadores
class PALADINO():
    """Configurações básicas paladino"""
    #Instancias de composição
    STATUS: ConfiguracaoStatus = ConfiguracaoStatus()
    STATUS_MAGO: ConfiguracaoMago =  ConfiguracaoMago()
    ATAQUE_BASICO: ConfiguracaoBasicaAtaque = ConfiguracaoBasicaAtaque()
    ATAQUE_ESPECIAL: ConfiguracaoBasicaAtaque =  ConfiguracaoBasicaAtaque()
    RECUPERAR_FOLEGO: RecuperarFolego = RecuperarFolego()


    #Status
    STATUS.NOME = 'paladino'
    STATUS.VIDA = 80
    STATUS_MAGO.MANA_MAXIMA = 10
    STATUS_MAGO.RESTAURACAO_MANA_CRITICO = 1
    

    #Ataque básico
    ATAQUE_BASICO.ID = 1
    ATAQUE_BASICO.DANO = 10
    ATAQUE_BASICO.MULTIPLICADOR_CRITICO = Combate.MULTIPLICADOR_CRITICO_PADRAO

    #Mensagens
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_CRITICO = f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_INICIO = "\nVocê segura sua espada com força, e vai pra cima do alvo, e..."
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_NORMAL = "\nVocê acerta seu golpe no alvo!\n"


    #Ataque especial
    ATAQUE_ESPECIAL.ID = 3
    ATAQUE_ESPECIAL.DANO = 25
    ATAQUE_ESPECIAL.CUSTO = 5
    
    #Mensagens
    ATAQUE_ESPECIAL.MENSAGENS.MENSAGEM_INICIO = f'\nVocê levanta sua espada, exibindo uma luz divina e vai pra cima do alvo com tudo o que tem, e...'
    ATAQUE_ESPECIAL.MENSAGENS.MENSAGEM_NORMAL = f'\nVocê acerta seu golpe no alvo!\n'
    ATAQUE_ESPECIAL.MENSAGENS.MENSAGEM_CRITICO = f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n'
    

    #Recuperar Folego
    RECUPERAR_FOLEGO.ID = 1
    RECUPERAR_FOLEGO.VIDA.TIPO_DADO = Dados.D10
    RECUPERAR_FOLEGO.VIDA.QUANTIDADE_DADOS = 2
    RECUPERAR_FOLEGO.MANA.QUANTIDADE = 1


class ASSASSINO(): 
    """Configurações da classe de Assassino"""

    NOME: str = 'Assassino'
    VIDA: int = 50
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

    STATUS = ConfiguracaoStatus()
    ATAQUE_BASICO = ConfiguracaoBasicaAtaque()

    STATUS.NOME= 'esqueleto'
    STATUS.VIDA= 10

    ATAQUE_BASICO.MULTIPLICADOR_CRITICO = Combate.MULTIPLICADOR_CRITICO_PADRAO

    ATAQUE_BASICO.ID = 1
    ATAQUE_BASICO.DANO = 4

    #Mensagens
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_CRITICO = f'\nELE TE ACERTA EM CHEIO!!!\n'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_FALHA = f'\nVocê consegue desviar do ataque a tempo!'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_INICIO = f'\nO esqueleto corre em sua direção com a espada levantada...'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_NORMAL = f'\nEle te corta.\n'


class LICH():
    """Configuroções da classe de Lich."""

    STATUS = ConfiguracaoStatus()
    ATAQUE_BASICO = ConfiguracaoBasicaAtaque()


    STATUS.NOME = 'Lich'
    STATUS.VIDA = 100
    ATAQUE_BASICO.MULTIPLICADOR_CRITICO = Combate.MULTIPLICADOR_CRITICO_PADRAO

    ATAQUE_BASICO.ID = 1
    ATAQUE_BASICO.DANO = 10
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_INICIO = f'\nO Lich levanta suas mãos, invocando um raio necromante...'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_FALHA = f'\nVocê consegue desviar da magia a tempo!'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_NORMAL = f'\nEle acerta o raio em você.\n'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_CRITICO = f'\nELE TE ACERTA EM CHEIO!!!\n'

    ID_INVOCAR_ESQUELETO: int = 2
    QUANTIDADE_ESQUELETOS_INVOCADOS: int = 1


class Menus:
    """Constantes de configurações de menus."""

    MENU_ATAQUE = 1
    MENU_BUFFS = 2