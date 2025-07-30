#Libs
from .Criatura import Criatura
from typing import Union, Callable


#Consts
YELLOW = '\033[93m'
RESET = '\033[0m'


class Jogador(Criatura):
    def __init__(self):
        self.nome = "jogador"
        self.vida = 70
        self.stamina = 10

        self.acoes_ataque: dict[int, Callable[[], int]] = {
            1: self.atacar,
            2: self.bola_de_fogo,
            3: self.ataque_especial
        }

        self.acoes_buff = {
            1: self.recuperar_folego
        }
    

    #Acoes
    def atacar(self) -> int:
        print('\nVocê segura sua espada com força, e vai pra cima do alvo, e...')
        self.contagem_regressiva(3)
        rolagem = self.rolarD6(1)
        if rolagem == 1:
            print('\nInfelizmente você erra o ataque.')
            return 0
        elif rolagem == 6:
            print(f'{YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 20 de dano]]\n[[Recuperou 1 de stamina]]{RESET}')
            self.stamina += 1
            return 20
        else:
            print('\nVocê acerta seu golpe no alvo!\n[[Causou 10 de dano]]')
            return 10


    def recuperar_folego(self) -> None:
        cura = self.rolarD8(2)
        print(f'\nVocê respira fundo e consegue recuperar parte da sua força.\n[[Curou {cura} de vida]]\n[[Recuperou 1 de stamina]]')
        self.vida += cura
        self.stamina += 1
        if self.vida > 70:
            self.vida = 70


    def ataque_especial(self) -> int:
        print('\nVocê levanta sua espada, exibindo uma luz divina e vai pra cima do alvo com tudo o que tem, e...')
        self.contagem_regressiva(3)
        self.stamina -= 15
        atkJ = self.rolarD6(1)
        if atkJ == 1:
            print('\nInfelizmente você erra o ataque.')
            return 0
        elif atkJ == 6:
            print(f'{YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 50 de dano]]{RESET}')
            return 50
        else:
            print('\nVocê acerta seu golpe no alvo!\n[[Causou 25 de dano]]')
            return 25


    def bola_de_fogo(self) -> int:
        if self.batalha == None:
            return 0
        print('\nVocê junta a suas mãos e começa a canalizar, uma energia magica começa a surgir e...')
        self.contagem_regressiva(3)
        rolagem = self.rolarD6(1)
        if rolagem == 1:
            print('\nA magia se desfaz no ar.')
            return 0
        elif rolagem == 6:
            print(f'{YELLOW}\nVocê acerta ela numa explosão enorme!!!\n[[Causou 10 de dano em todos os alvos]]\n[[Recuperou 1 de stamina]]{RESET}')
            self.stamina += 1
            for criatura in self.batalha.criaturas:
                if isinstance(criatura, Jogador):
                    continue
                criatura.vida -= 10
            return 0
        else:
            print('\nVocê acerta seu golpe e todos os inimigos sofrem queimaduras!\n[[Causou 5 de dano em todos os alvos]]')

            for criatura in self.batalha.criaturas:
                if isinstance(criatura, Jogador):
                    continue
                criatura.vida -= 5
            return 0


    #Menus
    def menu_ataque(self) -> None:
        if self.batalha == None:
            return

        print("1- Atacar (dano em 1 alvo)")
        print("2 - Bola de fogo (dano em área)")
        if self.stamina >= 15:
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

            if acao == self.acoes_ataque.get(3) and self.stamina < 15:
                print("Tá tentando burlar o esquema né princesa.")
                continue

            print("Escolha um alvo:")
            for index, alvo in enumerate(self.batalha.criaturas):
                print(f"{index} = {alvo.nome}")

            alvo = input()

            if not alvo.isdigit():
                print("Alvo inválido, turno perdido.")
                return
                
            alvo = int(alvo)
            if not self.batalha.criaturas[alvo]:
                print("Alvo inválido, turno perdido.")
                return
            
            valor = self.acoes_ataque[escolha]()
            self.batalha.criaturas[alvo].vida -= valor
            return

    
    def menu_buff(self) -> None:
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

        print('\nAgora é sua vez, o que deseja fazer?')
        print('1- Atacar')
        print('2- Se buffar')

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
                   self.menu_buff()
                   return
                case _:
                    print("Escolha fora dos limites, por favor tente novamente.")


    #Outros metodos
    def mostrar_stats(self) -> None:
        print('\nVida do Jogador: {}'.format(self.vida))
        print('Stamina do Jogador: {}'.format(self.stamina))
        print()

    
    def turno(self) -> Union[int, None]:
        self.menu_acoes()