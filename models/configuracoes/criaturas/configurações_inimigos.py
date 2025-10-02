#Configurações específicas de inimigos.
#libs
from typing import Union
from ....game_data.outras_configs import Combate
from interfaces import AtributosBase

#Classes
class ESQUELETO():
    """Configurações da classe Esqueleto."""
    def __init__(self) -> None:
        self.nome: str = 'esqueleto'
        
        self.atributos: AtributosBase = {
            'vida_maxima': 10,
            'vida_atual': 10
        }


        self.ataques: dict[str, dict[str, Union[str, int]]] = {
            'ataque_basico': {
                'id': 1,
                'dano': 4,
                'multiplicador_critico': Combate.MULTIPLICADOR_CRITICO_PADRAO,
                'mensagem_inicial': f'\nO esqueleto corre em sua direção com a espada levantada...',
                'mensagem_falha': f'\nVocê consegue desviar do ataque a tempo!',
                'mensagem_normal': f'\nEle te corta.\n',
                'mensagem_critico': f'\nELE TE ACERTA EM CHEIO!!!\n'
            }
        }


class LICH():
    """Configuroções da classe de Lich."""
    def __init__(self) -> None:
        self.nome: str = 'lich'


        self.atributos: AtributosBase = {
            'vida_maxima': 100,
            'vida_atual': 100,
        }


        self.ataques: dict[str, dict[str, Union[str, int]]] = {
            'ataque_basico': {
                'id': 1,
                'dano': 10,
                'multiplicador_critico': Combate.MULTIPLICADOR_CRITICO_PADRAO,
                'mensagem_inicio': f'\nO Lich levanta suas mãos, invocando um raio necromante...',
                'mensagem_falha': f'\nVocê consegue desviar da magia a tempo!',
                'mensagem_normal': f'\nEle acerta o raio em você.\n',
                'mensagem_critico': f'\nELE TE ACERTA EM CHEIO!!!\n',
                },

            'invocar_esqueleto': {
                'id': 2,
                'quantidade_invocacoes': 1,
                'multiplicador_critico': Combate.MULTIPLICADOR_CRITICO_PADRAO,
                'mensagem_inicio': f'\n O Lich toca na terra, fazendo-a tremer...',
                'mensagem_falha': f'\n Nada acontece',
                'mensagem_normal': f'\n esqueleto surge da terra.',
                'mensagem_critico': f'\n esqueletos surgem da terra!'
        }
        }