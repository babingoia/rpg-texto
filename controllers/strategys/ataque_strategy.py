#Algoritimos para selecionar um alvo.
#libs
from interfaces import IAtaqueStrategy, IAtaqueStrategyFactory, ICriatura, IData, IView
from helpers import convert_to_message
from random import randint
from typing import Any
from helpers import validar_chaves_dicionario

#Classes

class RandomAgressiveStrategy(IAtaqueStrategy):
    def __init__(self, conjurador: ICriatura) -> None:
        self.conjurador: ICriatura = conjurador


    def escolher_alvo(self, alvos: dict[str, list[ICriatura]]) -> ICriatura:
        inimigos: list[ICriatura] = []
        
        for lista in alvos.values():
            if self.conjurador in lista:
                continue

            inimigos = lista

        escolha = randint(0, len(inimigos) - 1)

        alvo = inimigos[escolha]

        return alvo
        

class PlayerStrategy(IAtaqueStrategy):
    def __init__(self, tela: IView) -> None:
        self.tela = tela

    def escolher_alvo(self, alvos: dict[str, list[ICriatura]]) -> ICriatura:
        mensagens: list[IData] = convert_to_message([{
                '': 'Deseja acertar um jogador ou um inimigo?'
            }, {'1': 'jogador'}, {'2': 'inimigo'}], 'BatalhaController')

        for mensagem in mensagens:
            self.tela.mostrar(mensagem)
        
        tipo_alvo = self.tela.get_input([1,2])

        if tipo_alvo == 1:
            tipo_alvo = 'jogadores'
        else:
            tipo_alvo = 'inimigos'
        
        mensagens = convert_to_message(
            {chave: criatura.get_nome() for chave, criatura in enumerate(alvos[tipo_alvo])},
            ' batalhaController.')
        
        for mensagem in mensagens:
            self.tela.mostrar(mensagem)

        escolha = self.tela.get_input()

        alvo = alvos[tipo_alvo][escolha]
        
        return alvo


class AtaqueStrategyFactory(IAtaqueStrategyFactory):
    @staticmethod
    def criar(tipo: str, **kwargs: Any) -> IAtaqueStrategy:
        match tipo:
            case 'jogador':
                validar_chaves_dicionario(kwargs, ['tela'],'AtaqueStrategyFactory')
                return PlayerStrategy(kwargs['tela'])
            case 'random_agressive':
                validar_chaves_dicionario(kwargs, ['conjurador'], 'AtaqueStrategyFactory')
                return RandomAgressiveStrategy(kwargs['conjurador'])
            case _:
                raise ValueError('Stratégia de ataque não determinada.')