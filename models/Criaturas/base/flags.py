#Classe base para um jogador.
from gerenciadores import Batalha
from commands import Command
from .criatura import Criatura
from typing import Callable


class Jogador(Criatura):
    """Classe base que possui lógicas genéricas para jogadores."""
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)


    def mostrar_stats(self) -> None:
        """Mostra os status do paladino"""
        print(f'\nVida do{self.nome}: {self.vida}')
        print(f'Mana do {self.nome}: {self.mana}')
        print()


    def menu_acoes(self, lista_acoes: dict[int, Callable[[], list[Command]]]) -> list[Command]:
        """Mostra as opções de ataque daquela classe."""
        print("Selecione uma ação:")
        for id, item in lista_acoes.items():
            print(f"{id} - {item.__name__}")
        comandos = self.gerenciar_menu(lista_acoes)
        return comandos
                

    def gerenciar_menu(self, lista_acoes: dict[int, Callable[[], list[Command]]]) -> list[Command]:
        """Gerencia a escolha de ataque feita pelo jogador."""
        if self.batalha == None:
            raise ValueError("Ops, não está em batalha!")
        
        while True:
            escolha = input()

            if not escolha.isdigit():
                print("Escolha inválida.")
                continue

            escolha = int(escolha)

            acao = lista_acoes.get(escolha)

            if not acao:
                print("Ação inválida.")
                continue

            comandos = lista_acoes[escolha]()
            
            return comandos


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
