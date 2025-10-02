#Algoritimos para selecionar um alvo.
#libs
from interfaces import IAtaqueStrategy, IAtaqueStrategyFactory, ICriatura, BatalhaInicioTurno, Escolhas, Escolha
from ..configurações import Cores
from random import randint
from typing import Any
from helpers import validar_chaves_dicionario
from inspect import signature

#Classes
class RandomAgressiveStrategy(IAtaqueStrategy):
    def __init__(self, conjurador: ICriatura) -> None:
        self.conjurador: ICriatura = conjurador


    def get_escolhas(self, data: BatalhaInicioTurno) -> Escolhas:
        nome_criatura = data["criatura_atual"].get_nome()
        escolhas: Escolhas

        print(f'{Cores.RESET} É a vez de {nome_criatura}')

        quantidade_acoes = len(data['acoes_disponiveis'].values())

        acao_escolhida = randint(1, quantidade_acoes)
        acao_escolhida = Escolha(acao_escolhida)
        inimigos: list[ICriatura] = data['criaturas']['jogadores']

        if 'alvos' in signature(data['acoes_disponiveis'][acao_escolhida.getValue()]).parameters:
            alvos = inimigos

            escolhas = {
                'acao_escolhida': acao_escolhida,
                'alvo_selecionado': alvos
            }

            return escolhas
        
        elif 'alvo' in signature(data['acoes_disponiveis'][acao_escolhida.getValue()]).parameters:

            escolha = randint(0, len(inimigos) - 1)

            alvo = inimigos[escolha]

            escolhas = {
                'acao_escolhida': acao_escolhida,
                'alvo_selecionado': [alvo]
            }

            return escolhas
        
        else:
            escolhas = {
                'acao_escolhida': acao_escolhida,
                'alvo_selecionado': None
            }

            return escolhas

        

class PlayerStrategy(IAtaqueStrategy):

    def get_escolha(self, minimo: int, maximo: int) -> Escolha:
        escolha: Escolha

        while True:
            valor = input()
            try:
                escolha = Escolha(valor)
            except:
                print('Ops, parece que você digitou um valor incorreto. Por favor tente novamente.')
                continue

            in_inteval = escolha.checar_intervalo(minimo, maximo)

            if not in_inteval:
                print('Hum... seu valor parece não estar no range.')
                continue

            return escolha


    def escolher_alvo(self, data: BatalhaInicioTurno) -> ICriatura:
        print(f"{Cores.RESET} Deseja selecionar qual tipo de alvo?")
        print(f'{Cores.GREEN} 1 - Aliados')
        print(f"{Cores.RED} 2 - Inimigos")

        tipo_alvo_escolha: Escolha = self.get_escolha(1, 2)

        tipo_alvo: str

        if tipo_alvo_escolha.getValue() == 1:
            tipo_alvo = 'jogadores'
        else:
            tipo_alvo = 'inimigos'
        
        print('Deseja selecionar qual alvo?')
        for index, alvo in enumerate(data['criaturas'][tipo_alvo]):
            print(f'{index}: {alvo.get_nome()}')
        
        alvo_escolha: Escolha = self.get_escolha(0, len(data['criaturas'][tipo_alvo]))

        alvo = data['criaturas'][tipo_alvo][alvo_escolha.getValue()]
        return alvo
            

    def get_escolhas(self, data: BatalhaInicioTurno) -> Escolhas:
        nome_criatura = data['criatura_atual'].get_nome()
        print(f'{Cores.RESET} É a vez de: {nome_criatura}, qual ação deseja tomar?')


        for index, acao in data['acoes_disponiveis'].items():
            print(f'{index}: {acao.__name__}')

        acao_escolhida = self.get_escolha(0, len(data['acoes_disponiveis']))

        if 'not_alvo' in signature(data['acoes_disponiveis'][acao_escolhida.getValue()]).parameters:
            escolhas: Escolhas = {
                'acao_escolhida': acao_escolhida,
                'alvo_selecionado': None
            }
            return escolhas 

        alvo = self.escolher_alvo(data)

        escolhas = {
            'acao_escolhida': acao_escolhida,
            'alvo_selecionado': [alvo]
        }
        
        return escolhas


class AtaqueStrategyFactory(IAtaqueStrategyFactory):
    @staticmethod
    def criar(tipo: str, **kwargs: Any) -> IAtaqueStrategy:
        match tipo:
            case 'jogador':
                return PlayerStrategy()
            case 'random_agressive':
                validar_chaves_dicionario(kwargs, ['conjurador'], 'AtaqueStrategyFactory')
                return RandomAgressiveStrategy(kwargs['conjurador'])
            case _:
                raise ValueError('Stratégia de ataque não determinada.')