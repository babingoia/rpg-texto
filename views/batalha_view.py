#View para batalhas.
#Libs
from interfaces import BatalhaData, BatalhaFinal, BatalhaFinalTurno, BatalhaInicioTurno, IBatalhaSubscriber, IAtaqueStrategyFactory, ICriatura
from .base.view import View
from .strategys import AtaqueStrategyFactory
from .configurações import Cores

#Classe
class BatalhaView(View, IBatalhaSubscriber):
    """Tela do fluxo de batalha.""" 
    def __init__(self, strategy_factory: IAtaqueStrategyFactory= AtaqueStrategyFactory()) -> None:
        super().__init__()
        self.strategy_factory = strategy_factory


    def mostrar_atributos(self, criaturas: list[ICriatura], cor: str, titulo: str) -> None:

        print(f"{cor} {titulo}:\n")
        for criatura in criaturas:
            atributos = criatura.get_atributos()
            print(f'\n {cor}{criatura.get_nome()} \n:')
            
            for atributo, valor in atributos.items():
                if atributo.endswith('_maxima') or atributo.endswith('_maximo'):
                    continue

                atributo = atributo.replace('_atual', ' ')
                atributo = atributo.replace('_', ' ')
                print(f"{cor}{atributo}: {valor}")


    def mostrar_status_globais(self, data: BatalhaData):
        print(f'{Cores.RESET} Todos se movem rapidamente, os turnos ficam nessa ordem:\n')
        
        for criatura in data['ordem_turnos']:
            print(f'{Cores.BLUE}{criatura.get_nome()}')
        
        print(f'{Cores.RESET} \n Status das Criaturas: \n')

        self.mostrar_atributos(data['inimigos'], Cores.RED, 'Inimigos')
        self.mostrar_atributos(data['jogadores'], Cores.GREEN, 'Aliados')
        
        input("Pressione enter para continuar...")


    def battle_start_update(self, data: BatalhaData) -> None:
        print(f"{Cores.RESET} Vocês foram encurralados por: ")
        
        for inimigo in data['inimigos']:
            print(f'{Cores.RED}{inimigo.get_nome()}')
        
        print(f'{Cores.RESET}')
        self.contagem_regressiva(3)
        print(f'{Cores.RED}E não há mais como escapar!')
        input('Digite enter para continuar...')
        self.limpar_tela()

    

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
