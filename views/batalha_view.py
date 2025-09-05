#View para batalhas.
#Libs
from interfaces import BatalhaData, BatalhaFinal, BatalhaFinalTurno, BatalhaInicioTurno, IBatalhaSubscriber, IAtaqueStrategyFactory
from .base.view import View
from .strategys import AtaqueStrategyFactory
from .configurações import Cores

#Classe
class BatalhaView(View, IBatalhaSubscriber):
    """Tela do fluxo de batalha.""" 
    def __init__(self, strategy_factory: IAtaqueStrategyFactory= AtaqueStrategyFactory()) -> None:
        super().__init__()
        self.strategy_factory = strategy_factory


    def mostrar_status_globais(self, data: BatalhaData):
        print(f'{Cores.RESET} Todos se movem rapidamente, os turnos ficam nessa ordem:\n')
        
        for criatura in data['ordem_turnos']:
            print(f'{Cores.BLUE}{criatura.get_nome()}')
        
        print(f'{Cores.RESET} \n Status das Criaturas: \n')

        print(f"{Cores.RED} Inimigos:\n")
        for inimigo in data['inimigos']:
            atributos = inimigo.get_atributos()
            print(f'{Cores.RED}{inimigo.get_nome()}:')
            
            for atributo, valor in atributos.items():
                if atributo.endswith('_maxima') or atributo.endswith('_maximo'):
                    continue

                atributo = atributo.replace('_atual', ' ')
                print(f"{Cores.RED}{atributo}: {valor}")
        

        print(f'{Cores.GREEN} \n Jogadores: \n')
        for jogador in data['jogadores']:
            atributos = jogador.get_atributos()
            print(f'{Cores.GREEN}{jogador.get_nome()}')

            for atributo, valor in atributos.items():
                if atributo.endswith('_maxima') or atributo.endswith('_maximo'):
                    continue

                atributo = atributo.replace('_atual', ' ')
                print(f'{Cores.GREEN}{atributo}: {valor}')
        
        input("Pressione enter para continuar...")


    def battle_start_update(self, data: BatalhaData) -> None:
        print(f"{Cores.RESET} Vocês foram encurralados por: ")
        
        for inimigo in data['inimigos']:
            print(f'{Cores.RED}{inimigo.get_nome()}')
        
        print(f'{Cores.RESET}')
        self.contagem_regressiva(3)
        print(f'{Cores.RED}E não há mais como escapar!')
        input('Digite enter para continuar...')

    

    def battle_end_update(self, data: BatalhaFinal) -> None:
        pass


    def turn_start_update(self, data: BatalhaInicioTurno) -> None:

        self.mostrar_status_globais(data['criaturas'])

        if data['criatura_atual'] in data['criaturas']['inimigos']:
            strategy = self.strategy_factory.criar('random_agressive', conjurador=data['criatura_atual'])
            escolhas = strategy.get_escolhas(data)
        else:
            strategy = self.strategy_factory.criar('jogador')
            escolhas = strategy.get_escolhas(data)

        self.get_input_notify(escolhas)
    

    def turn_end_update(self, data: BatalhaFinalTurno) -> None:
        #Comparação de criaturas do turn_start com as de agora pra anunciar as mortes.
        self.limpar_tela()
