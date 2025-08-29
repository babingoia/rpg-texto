#Controi as telas de batalhas.
#libs
from interfaces import IView, IData
from os import name, system
from typing import Any, cast
from time import sleep

#Classes
class View (IView):
    """Gerencia a tela de batalha"""
    def __init__(self) -> None:
        pass


    def mostrar(self, dados: IData) -> None:
        mensagem: dict[Any, Any] = dados.get_data()
        cast(dict[str, str], mensagem)

        for nome, valor in mensagem.items():
            nome.replace('_', ' ')
            print(f'{nome}: {valor}')

    
    def get_input(self, check: list[int] | None = None) -> int:
        while True:
            escolha = input()

            escolha.strip()

            if escolha.isdigit() == False:
                print('Ops, sua escolha não contem apenas números!')
                continue

            escolha = int(escolha)

            if check == None:
                return escolha

            if escolha < 0 or escolha >= check.__len__():
                print('Escolha inválida, por favor tente novamente!')
                continue

            return escolha

    
    def limpar_tela(self) -> None:
        if name == 'nt':
            system('cls')
        else:
            system('clear')


    def contagem_regressiva(self, segundos: int) -> None:
        """Inicia uma contagem regressiva.
        
        Args:
            segundos: quantidade de segundos que a contagem vai demorar.
        """
        for i in range(segundos, 0, -1):
            print(f"{i}...", end=' ', flush=True)
            sleep(1)
        print('\n')