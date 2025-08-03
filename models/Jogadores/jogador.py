#Classe base para um jogador.
from models.Gerenciadores.batalha import Batalha
#from typing import TYPE_CHECKING
from configs import Menus
from ..Criatura import Criatura


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


    def menu_ataque(self) -> None:
        """Mostra as opções de ataque daquela classe."""
        print("Selecione uma ação de ataque:")
        for id, item in self.acoes_ataque.items():
            print(f"{id} - {item.__name__}")
        self.gerenciar_menu_ataque()


    def menu_acoes(self) -> None:
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

            match escolha:
                case Menus.MENU_ATAQUE:
                    self.menu_ataque()
                    return None
                case Menus.MENU_BUFFS:
                   self.menu_buffs()
                   return None
                case _:
                    print("Escolha fora dos limites, por favor tente novamente.")
                    return None


    def gerenciar_menu_ataque(self) -> None:
        """Gerencia a escolha de ataque feita pelo jogador."""
        if self.batalha == None:
            return
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
            
            while True:
                alvo = input()

                if not alvo.isdigit():
                    print("Alvo inválido, tente novamente.")
                    continue
                
                alvo = int(alvo)

                if not (0 <= alvo < len(self.batalha.inimigos)):
                    print("Alvo inválido, tente novamente.")
                    continue
            
                valor = self.acoes_ataque[escolha]()
                self.batalha.inimigos[alvo].vida -= valor
                return


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


    def escolher_alvo(self):
        pass