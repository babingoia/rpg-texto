#Data dos ataques.
#libs
from .outras_configs import Combate
from 

#Data
class Ataques:

    ATAQUE_BASICO = {
        
        'id': 1,
        'dano': 10,
        'multiplicador_critico': Combate.MULTIPLICADOR_CRITICO_PADRAO,
        'recuperacao_mana_critico': 1,

        'Ataque_'

        'mensagem_inicio': f'\nVocê segura sua espada com força, e vai pra cima do alvo, e...' ,
        'mensagem_falha': f'\nVocê erra o ataque.',
        'mensagem_normal': f'\nVocê acerta seu golpe no alvo!\n' ,
        'mensagem_critico': f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n' ,
    }
