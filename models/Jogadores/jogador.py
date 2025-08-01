#Classe base para um jogador.
from models.batalha import Batalha
from ..Criatura import Criatura


class Jogador(Criatura):
    """Classe base que possui lógicas genéricas para jogadores."""
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)
    
    def menu_buffs(self) -> None:
        """Mostra as opções de buff daquela classe. Precisa ser implementado na classe específica."""
        pass


    def menu_ataque(self) -> None:
        """Mostra as opções de ataque daquela classe. Precisa ser implementado na classe específica."""
        pass


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
                case 1:
                    self.menu_ataque()
                    return
                case 2:
                   self.menu_buffs()
                   return
                case _:
                    print("Escolha fora dos limites, por favor tente novamente.")


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