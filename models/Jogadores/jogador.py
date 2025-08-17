#Classe base para um jogador.
from models.Gerenciadores.batalha import Batalha
#from typing import TYPE_CHECKING
from ..Configs.configs import Menus
from ..Criatura import Criatura
from ..Ataques.Commands import Command


class Jogador(Criatura):
    """Classe base que possui lógicas genéricas para jogadores."""
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)


    def mostrar_stats(self) -> None:
        """Mostra os status do paladino"""
        print(f'\nVida do{self.nome}: {self.vida}')
        print(f'Mana do {self.nome}: {self.mana}')
        print()

 
    def menu_buffs(self) -> None:
        """Mostra as opções de buff daquela classe."""
        print("Selecione uma ação de ataque:")
        for id, item in self.acoes_buff.items():
            print(f"{id} - {item.__name__}")
        self.gerenciar_menu_buffs()


    def menu_ataque(self) -> list[Command]:
        """Mostra as opções de ataque daquela classe."""
        print("Selecione uma ação de ataque:")
        for id, item in self.acoes_ataque.items():
            print(f"{id} - {item.__name__}")
        comandos = self.gerenciar_menu_ataque()
        return comandos


    def menu_acoes(self) -> list[Command]:
        """Cria um menu básico para o jogador escolher entre as ações que deseja executar."""

        print(f'\nAgora é sua vez {self.nome}, o que deseja fazer?')
        print('1- Atacar')
        print('2- Se buffar')

        while True:
            escolha = input()

            if not escolha.isdigit():
                print("Escolha inválida, por favor tente novamente.")
                continue

            escolha = int(escolha)

            """
            match escolha:
                case Menus.MENU_ATAQUE:
                    comandos = self.menu_ataque()
                case Menus.MENU_BUFFS:
                   self.menu_buffs()
                case _:
                    print("Escolha fora dos limites, por favor tente novamente.")
                    continue
                """
            if escolha == Menus.MENU_ATAQUE:
                comandos = self.menu_ataque()
            else:
                print("Escolha fora dos limites, por favor tente novamente.")
                continue
            return comandos
                

    def gerenciar_menu_ataque(self) -> list[Command]:
        """Gerencia a escolha de ataque feita pelo jogador."""
        if self.batalha == None:
            raise ValueError("Ops, não está em batalha!")
        
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

            valor = self.acoes_ataque[escolha]()
            
            return valor


    def gerenciar_menu_buffs(self) -> None:
        """Gerencia a escolha feita de buffs do jogador."""
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


    def escolher_alvo(self) -> Criatura:
        if self.batalha == None:
            raise ValueError("Ops, não está em batalha!")
        
        print("Escolha um alvo:")
        for index, alvo in enumerate(self.batalha.inimigos):
            print(f"{index} = {alvo.nome}")
        
        while True:
            alvo = input()

            if not alvo.isdigit():
                print("Alvo inválido, tente novamente.")
                continue
            
            alvo = int(alvo)

            if not (0 <= alvo < len(self.batalha.inimigos)):
                print("Alvo inválido, tente novamente.")
                continue

            return self.batalha.inimigos[alvo]


class IA(Criatura):
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)
    

    def escolher_alvo(self) -> Criatura:
        
        if self.batalha == None:
            raise ValueError("Ops, não existe combate!")
        
        alvo = next((i for i,a in enumerate(self.batalha.jogadores) if isinstance(a, Jogador)), None)
        
        if alvo == None:
            raise ValueError("Jogador não encontrado.")
        return self.batalha.jogadores[alvo]