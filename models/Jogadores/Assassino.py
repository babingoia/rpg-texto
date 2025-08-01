#Classe para o assassino
#Libs
from ...consts import YELLOW, RESET
from models.batalha import Batalha
from .jogador import Jogador
from typing import Callable


#classes
class Asssassino(Jogador):
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)
        self.nome = "Assassino"
        self.vida = 50
        self.acoes_ataque: dict[int, Callable[[], int]] = {
            1: self.atacar,
            2: self.ataque_area,
            3: self.ataque_especial
        }
        self.acoes_buff: dict[int, Callable[[], None]] = {}
    

    def atacar(self) -> int:
        print(f'\nVocê se move rapidamente com sua adaga, vai pra cima da criatura, e...')
        self.contagem_regressiva(3)
        atkJ = self.rolar_dados(6, 1)
        if atkJ == 1:
            print('\nInfelizmente você erra o ataque.')
            return 0
        elif atkJ == 6:
            print(f'{YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 24 de dano]]\n[[Recuperou 12 de vida]]{RESET}')
            self.vida += 8
            return 24
        else:
            print(f'\nVocê acerta seu golpe na criatura!\n[[Causou 12 de dano]]\n[[Recuperou 6 de vida]]')
            self.vida += 4
            return 12


    def ataque_especial(self) -> int:
        print('\nVocê ergue sua adaga, faz um corte em sua mão para que ela se alimente de seu sangue, e avança enquanto sua arma brilha em vermelho...')
        self.contagem_regressiva(3)
        atkJ = self.rolar_dados(6, 1)
        if atkJ == 1:
            print('\nInfelizmente você erra o ataque.\n[[Perdeu 4 de vida]]')
            self.vida -= 4
            return 0
        elif atkJ == 6:
            print(f'{YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 56 de dano]]{RESET}')
            return 56
        else:
            print(f'\nVocê acerta seu golpe na criatura!\n[[Causou 28 de dano]]\n[[Perdeu 4 de vida]]')
            self.vida -= 4
            return 28


    def ataque_area(self) -> int:
        if self.batalha == None:
            return 0 # So pra n dar erro na IDE
        cura: int = 0
        dano: int = 0
        print('\nVocê avança com sua adaga, fazendo movimentos rápidos e mirando em todos em sua frente...')
        self.contagem_regressiva(3)
        atkJ = self.rolar_dados(6, 1)
        if atkJ == 1:
            print('\nInfelizmente você erra o ataque.')
        elif atkJ == 6:
            dano = 12
            cura = 4
            print(f'{YELLOW}\nVocê acerta um golpe crítico em todos os inimigos!!!\n[[Causou {dano} de dano a todos]]\n[[Recuperou {cura} de vida]]{RESET}')
        else:
            dano = 6
            cura = 2
            print(f'\nVocê acerta seu golpe em todos os inimigos!\n[[Causou {dano} de dano a todos]]\n[[Recuperou {cura} de vida]]')

        self.vida += cura
        for inimigo in self.batalha.inimigos:
            inimigo.vida -= dano
        
        return 0 # So pra n dar erro na IDE


#Menus
    def menu_ataque(self) -> None:
        """Cria um menu para a escolha de ações de ataque."""
        print("1- Atacar (dano em 1 alvo)")
        print("2- Ataque em área")
        print('3- ATAQUE ESPECIAL disponível! (25 de dano normal/50 de dano crítico)')
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