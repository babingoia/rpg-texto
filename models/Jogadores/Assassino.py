#Classe para o assassino
#Libs
from models.batalha import Batalha
from .jogador import Jogador
from typing import Callable


#Consts
YELLOW = '\033[93m'
RESET = '\033[0m'


#classes
class Asssassino(Jogador):
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)
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
        if self.batalha == None:
            return

        print("1- Atacar (dano em 1 alvo)")
        print("2- Ataque em área")
        print('3- ATAQUE ESPECIAL disponível! (25 de dano normal/50 de dano crítico)')
        
        while True:
            escolha = input()

            if not escolha.isdigit():
                print("Escolha inválida.")
                continue

            escolha = int(escolha)

            acao = self.acoes_ataque.get(escolha)

            if not acao:
                print("Ação inválida.")
                continue

            print("Escolha um alvo:")
            for index, alvo in enumerate(self.batalha.inimigos):
                print(f"{index} = {alvo.nome}")

            alvo = input()

            if not alvo.isdigit():
                print("Alvo inválido, turno perdido.")
                return
                
            alvo = int(alvo)
            if not self.batalha.inimigos[alvo]:
                print("Alvo inválido, turno perdido.")
                return
            
            valor = self.acoes_ataque[escolha]()
            self.batalha.inimigos[alvo].vida -= valor
            return

    
    def menu_buff(self) -> None:
        """Cria um menu para a escolha de ações de buff."""
        print("1 - Se recuperar (Se cura em 2d8 e + 1 de stamina)")
        while True:
            escolha = input()

            if not escolha.isdigit():
                print("Escolha inválida.")
                continue

            escolha = int(escolha)

            acao = self.acoes_buff.get(escolha)

            if not acao:
                print("Ação inválida.")
                continue

            self.acoes_buff[escolha]()
            return


    def menu_acoes(self) -> None:
        """Cria um menu básico para o jogador escolher entre as ações que deseja executar."""

        print('\nAgora é sua vez, o que deseja fazer?')
        print('1- Atacar')

        while True:
            escolha = input()

            if not escolha.isdigit():
                print("Escolha inválida, por favor tente novamente.")
                continue

            escolha = int(escolha)

            match escolha:
                case 1:
                    self.menu_ataque()
                    return
                case 2:
                   # self.menu_buff() -> nao existe nenhum ainda
                   return
                case _:
                    print("Escolha fora dos limites, por favor tente novamente.")


    #Outros metodos
    def mostrar_stats(self) -> None:
        """Mostra os status do paladino"""
        print('\nVida do Assassino: {}'.format(self.vida))
        print()


    def turno(self):
        self.menu_acoes()