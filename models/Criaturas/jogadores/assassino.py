#Classe para o assassino
#Libs
from gerenciadores import Batalha
from ..base import Jogador
from typing import Callable
from configuracoes import ASSASSINO, Cores, Combate


#classes
class Assassino(Jogador):
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)
        self.nome = ASSASSINO.NOME
        self.vida: int = ASSASSINO.VIDA
        self.acoes_ataque: dict[int, Callable[[], int]] = {
            ASSASSINO.ID_ATAQUE_BASICO: self.atacar,
            ASSASSINO.ID_ATAQUE_AREA: self.ataque_area,
            ASSASSINO.ID_ATAQUE_ESPECIAL: self.ataque_especial
        }
        self.acoes_buff: dict[int, Callable[[], None]] = {}
    

    def atacar(self) -> int:
        print(f'\nVocê se move rapidamente com sua adaga, vai pra cima da criatura, e...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        atkJ = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        
        if atkJ == Combate.FALHA:
            print('\nInfelizmente você erra o ataque.')
            return Combate.DANO_FALHA
        
        elif atkJ == Combate.CRITICO:
            print(f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 24 de dano]]\n[[Recuperou 12 de vida]]{Cores.RESET}')

            self.vida += ASSASSINO.CURA_ATAQUE_BASICO * ASSASSINO.MULTIPLICADOR_CRITICO

            return ASSASSINO.DANO_ATAQUE_BASICO * ASSASSINO.MULTIPLICADOR_CRITICO
        
        else:
            print(f'\nVocê acerta seu golpe na criatura!\n[[Causou 12 de dano]]\n[[Recuperou 6 de vida]]')
            self.vida += ASSASSINO.CURA_ATAQUE_BASICO
            return ASSASSINO.DANO_ATAQUE_BASICO


    def ataque_especial(self) -> int:
        print('\nVocê ergue sua adaga, faz um corte em sua mão para que ela se alimente de seu sangue, e avança enquanto sua arma brilha em vermelho...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        atkJ = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        
        if atkJ == Combate.FALHA:
            print('\nInfelizmente você erra o ataque.\n[[Perdeu 4 de vida]]')
            self.vida -= ASSASSINO.CUSTO_ATAQUE_ESPECIAL
            return Combate.DANO_FALHA
        
        elif atkJ == Combate.CRITICO:
            print(f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 56 de dano]]{Cores.RESET}')
            return ASSASSINO.DANO_ATAQUE_ESPECIAL * ASSASSINO.MULTIPLICADOR_CRITICO
        
        else:
            print(f'\nVocê acerta seu golpe na criatura!\n[[Causou 28 de dano]]\n[[Perdeu 4 de vida]]')
            self.vida -= ASSASSINO.CUSTO_ATAQUE_ESPECIAL
            return ASSASSINO.DANO_ATAQUE_ESPECIAL


    def ataque_area(self) -> int:
        if self.batalha == None:
            return 0 # So pra n dar erro na IDE
        cura: int = Combate.DANO_FALHA
        dano: int = Combate.DANO_FALHA
        print('\nVocê avança com sua adaga, fazendo movimentos rápidos e mirando em todos em sua frente...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        atkJ = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        
        if atkJ == Combate.FALHA:
            print('\nInfelizmente você erra o ataque.')
        
        elif atkJ == Combate.CRITICO:
            dano *= ASSASSINO.MULTIPLICADOR_CRITICO
            cura *= ASSASSINO.MULTIPLICADOR_CRITICO
            print(f'{Cores.YELLOW}\nVocê acerta um golpe crítico em todos os inimigos!!!\n[[Causou {dano} de dano a todos]]\n[[Recuperou {cura} de vida]]{Cores.RESET}')
        
        else:
            dano = ASSASSINO.DANO_ATAQUE_AREA
            cura = ASSASSINO.CURA_ATAQUE_AREA
            print(f'\nVocê acerta seu golpe em todos os inimigos!\n[[Causou {dano} de dano a todos]]\n[[Recuperou {cura} de vida]]')

        self.vida += cura
        for inimigo in self.batalha.inimigos:
            inimigo.vida -= dano
        
        return 0 # So pra n dar erro na IDE


#Menus
    def menu_ataque(self) -> None:
        """Cria um menu para a escolha de ações de ataque."""
        print(f"{ASSASSINO.ID_ATAQUE_BASICO}- Atacar (dano em 1 alvo)")
        print(f"{ASSASSINO.ID_ATAQUE_AREA}- Ataque em área")
        print(f'{ASSASSINO.ID_ATAQUE_ESPECIAL}- ATAQUE ESPECIAL disponível! (25 de dano normal/50 de dano crítico)')
        self.gerenciar_menu_ataque()

    
    def menu_buffs(self) -> None:
        """Cria um menu para a escolha de ações de buff."""
        pass


    #Outros metodos
    def mostrar_stats(self) -> None:
        """Mostra os status do paladino"""
        print('\nVida do Assassino: {}'.format(self.vida))
        print()


    def turno(self):
        self.menu_acoes()