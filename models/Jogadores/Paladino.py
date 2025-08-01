# Classe Paladino
#Libs
from ...configs import Configuracoes as cfg
from .jogador import Jogador
from typing import Union, Callable


class Paladino(Jogador):
    """Classe especifica para criar um paladino."""
    def __init__(self):
        """Cria uma instância de paladino com suas características básicas."""
        super().__init__()
        self.nome = "paladino"
        self.vida = 80
        self.mana = 0

        #Esse distinção de ações é importante por conta que umas precisam de alvo e outras não.
        self.acoes_ataque: dict[int, Callable[[], int]] = {
            1: self.atacar,
            2: self.bola_de_fogo,
            3: self.ataque_especial
        }

        self.acoes_buff: dict[int, Callable[[], None]] = {
            1: self.recuperar_folego
        }

        

    #Acoes
    def atacar(self) -> int:
        """Ataque básico do paladino em combate."""
        print('\nVocê segura sua espada com força, e vai pra cima do alvo, e...')
        self.contagem_regressiva(3)
        rolagem = self.rolar_dados(6, 1)
        if rolagem == 1:
            print('\nInfelizmente você erra o ataque.')
            return 0
        elif rolagem == 6:
            print(f'{cfg.Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 20 de dano]]\n[[Recuperou 1 de stamina]]{cfg.Cores.RESET}')
            self.mana += 1
            return 20
        else:
            print('\nVocê acerta seu golpe no alvo!\n[[Causou 10 de dano]]')
            return 10


    def recuperar_folego(self) -> None:
        """Ação de cura do paladino em combate."""
        cura = self.rolar_dados(10,2)
        print(f'\nVocê respira fundo e consegue recuperar parte da sua força.\n[[Curou {cura} de vida]]\n[[Recuperou 1 de stamina]]')
        self.vida = min(self.vida + cura, 80)
        self.mana += 1


    def ataque_especial(self) -> int:
        """Ataque especial do paladino em combate."""
        if self.mana < 5:
            print("Mana insuficiente! Turno perdido...")
            return 0
        print('\nVocê levanta sua espada, exibindo uma luz divina e vai pra cima do alvo com tudo o que tem, e...')
        self.contagem_regressiva(3)
        self.mana -= 5
        atkJ = self.rolar_dados(6, 1)
        if atkJ == 1:
            print('\nInfelizmente você erra o ataque.')
            return 0
        elif atkJ == 6:
            print(f'{cfg.Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 50 de dano]]{cfg.Cores.RESET}')
            return 50
        else:
            print('\nVocê acerta seu golpe no alvo!\n[[Causou 25 de dano]]')
            return 25


    def bola_de_fogo(self) -> int:
        """Ataque em área do paladino em combate."""
        if self.batalha == None:
            return 0
        print('\nVocê junta a suas mãos e começa a canalizar, uma energia magica começa a surgir e...')
        self.contagem_regressiva(3)
        rolagem = self.rolar_dados(6, 1)
        if rolagem == 1:
            print('\nA magia se desfaz no ar.')
            return 0
        elif rolagem == 6:
            print(f'{cfg.Cores.YELLOW}\nVocê acerta ela numa explosão enorme!!!\n[[Causou 10 de dano em todos os alvos]]\n[[Recuperou 1 de stamina]]{cfg.Cores.RESET}')
            self.mana += 1
            for inimigo in self.batalha.inimigos:
                inimigo.vida -= 10
            return 0
        else:
            print('\nVocê acerta seu golpe e todos os inimigos sofrem queimaduras!\n[[Causou 5 de dano em todos os alvos]]')

            for inimigo in self.batalha.inimigos:
                inimigo.vida -= 5
            return 0


    #Menus
    def menu_ataque(self) -> None:
        """Cria um menu para a escolha de ações de ataque."""
        print("1- Atacar (dano em 1 alvo)")
        print("2 - Bola de fogo (dano em área)")
        if self.mana >= 5:
            print('3- ATAQUE ESPECIAL disponível! (25 de dano normal/50 de dano crítico)')
        self.gerenciar_menu_ataque()

    
    def menu_buffs(self) -> None:
        """Cria um menu para a escolha de ações de buff."""
        print("1 - Se recuperar (Se cura em 2d8 e + 1 de stamina)")
        self.gerenciar_menu_buffs()


    #Outros metodos
    def mostrar_stats(self) -> None:
        """Mostra os status do paladino"""
        print('\nVida do Paladino: {}'.format(self.vida))
        print('Mana do Paladino: {}'.format(self.mana))
        print()

    
    def turno(self) -> Union[int, None]:
        """Gerencia o turno do paladino em combate."""
        self.menu_acoes()