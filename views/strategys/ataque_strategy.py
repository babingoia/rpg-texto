#Algoritimos para selecionar um alvo.
#libs
from interfaces import IAtaqueStrategy, IAtaqueStrategyFactory, ICriatura, BatalhaInicioTurno, Escolhas, Escolha
from ..configurações import Cores
from random import randint
from typing import Any
from helpers import validar_chaves_dicionario
from inspect import signature

#Classes
class BaseAtaqueStrategy(IAtaqueStrategy):
    pass


class RandomAgressiveStrategy(IAtaqueStrategy):
    def __init__(self, conjurador: ICriatura) -> None:
        self.conjurador: ICriatura = conjurador


    def get_escolhas(self, data: BatalhaInicioTurno) -> Escolhas:
        nome_criatura = data["criatura_atual"].get_nome()
        escolhas: Escolhas

        print(f'{Cores.RESET} É a vez de {nome_criatura}')

        quantidade_acoes = len(data['acoes_disponiveis'].values())

        acao_escolhida = randint(1, quantidade_acoes)

        if 'not_alvo' in signature(data['acoes_disponiveis'][acao_escolhida]).parameters:
            escolhas = {
                'acao_escolhida': Escolha(acao_escolhida),
                'alvo_selecionado': None
            }

            return escolhas

        inimigos: list[ICriatura] = data['criaturas']['jogadores']

        escolha = randint(0, len(inimigos) - 1)

        alvo = inimigos[escolha]

        escolhas = {
            'acao_escolhida': Escolha(acao_escolhida),
            'alvo_selecionado': alvo
        }

        return escolhas
        

class PlayerStrategy(IAtaqueStrategy):

    def escolher_acao(self, data: BatalhaInicioTurno) -> Escolha:
        while True:
            escolha = input()
            
            try:
                escolha = Escolha(escolha)
            except:
                print('Escolha de ação inválida, por favor digite apenas números.')
                continue

            if escolha.getValue() >= 0 and escolha.getValue() <= len(data['acoes_disponiveis']):
                break
        
        return escolha


    def escolher_alvo(self, data: BatalhaInicioTurno) -> ICriatura:
        print(f"{Cores.RESET} Deseja selecionar qual tipo de alvo?")
        print(f"{Cores.GREEN} 1 - Aliados")
        print(f"{Cores.RED} 2 - Inimigos")

        tipo_alvo: str
        while True:
            tipo_alvo_escolha = Escolha(input())
            
            if tipo_alvo_escolha.getValue() == 1:
                tipo_alvo = 'jogadores'

            elif tipo_alvo_escolha.getValue() == 2:
                tipo_alvo = 'inimigos'
            
            else:
                print('Ops, parece que você digitou um valor incorreto.')
                continue

            break

        
        print('Deseja selecionar qual alvo?')
        for index, alvo in enumerate(data['criaturas'][tipo_alvo]):
            print(f'{index}: {alvo.get_nome()}')
        
        alvo_escolha: Escolha
        while True:
            try:
                alvo_escolha = Escolha(input())
            except:
                print('Ops, alvo inválido! Por favor digite apenas números.')
                continue
            
            if alvo_escolha.getValue() < 0 or alvo_escolha.getValue() > len(data['criaturas'][tipo_alvo]):
                print('Hum... alvo fora do range, por favor digite o valor correto.')
                continue
            
            break

        alvo = data['criaturas'][tipo_alvo][alvo_escolha.getValue()]
        return alvo
            

    def get_escolhas(self, data: BatalhaInicioTurno) -> Escolhas:
        nome_criatura = data['criatura_atual'].get_nome()
        print(f'{Cores.RESET} É a vez de: {nome_criatura}, qual ação deseja tomar?')


        for index, acao in data['acoes_disponiveis'].items():
            print(f'{index}: {acao.__name__}')

        acao_escolhida = self.escolher_acao(data)

        if 'not_alvo' in signature(data['acoes_disponiveis'][acao_escolhida.getValue()]).parameters:
            escolhas: Escolhas = {
                'acao_escolhida': acao_escolhida,
                'alvo_selecionado': None
            }
            return escolhas 

        alvo = self.escolher_alvo(data)
        

        escolhas = {
            'acao_escolhida': acao_escolhida,
            'alvo_selecionado': alvo
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