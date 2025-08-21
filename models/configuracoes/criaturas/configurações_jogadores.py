#Configurações específicas para jogadores.
#libs
from ..outras_configs import Combate, Dados
from dataclasses import dataclass


#Jogadores
@dataclass
class PALADINO():
    """Configurações básicas paladino"""
    #Instancias de composição
    def __init__(self) -> None:
        self.NOME: str = 'paladino'
        self.ATRIBUTOS: dict[str, int] = {
            'vida_maxima': 80,
            'vida_atual': 80,
            'mana_maxima': 10,
            'mana_atual': 0,
            'restauracao_mana_critico': 1,
        }

        self.ATAQUE_BASICO: dict[str, int] = {
            'id': 1,
            'dano': 10,
            'multiplicador_critico': Combate.MULTIPLICADOR_CRITICO_PADRAO
        }

        self.ATAQUE_ESPECIAL: dict[str, int] = {
            'id': 2,
            'dano': 25,
            'custo': 5,
            'multiplicador_critico': Combate.MULTIPLICADOR_CRITICO_PADRAO
        }

        self.RECUPERAR_FOLEGO: dict[str, int] = {
            'id': 3,
            'tipo_dado': Dados.D10,
            'quantidade_dados': 2,
            'restauracao_mana_quantidade': 1
        }

"""        #Mensagens
        self.ATAQUE_BASICO.MENSAGENS.MENSAGEM_CRITICO = f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n'
        self.ATAQUE_BASICO.MENSAGENS.MENSAGEM_INICIO = "\nVocê segura sua espada com força, e vai pra cima do alvo, e..."
        self.ATAQUE_BASICO.MENSAGENS.MENSAGEM_NORMAL = "\nVocê acerta seu golpe no alvo!\n"
        
        #Mensagens
        self.ATAQUE_ESPECIAL.MENSAGENS.MENSAGEM_INICIO = f'\nVocê levanta sua espada, exibindo uma luz divina e vai pra cima do alvo com tudo o que tem, e...'
        self.ATAQUE_ESPECIAL.MENSAGENS.MENSAGEM_NORMAL = f'\nVocê acerta seu golpe no alvo!\n'
        self.ATAQUE_ESPECIAL.MENSAGENS.MENSAGEM_CRITICO = f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n'
        

        self.RECUPERAR_FOLEGO.MENSAGENS.MENSAGEM_INICIO = f'Você se acalma e fecha os olhos, uma pequena aura dourada se forma em torno de seu corpo e você se sente melhor.'"""


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