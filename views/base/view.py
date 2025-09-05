#Controi as telas de batalhas.
#libs
from interfaces import IView, Escolha, IViewSubject, IViewSubscriber, Escolhas
from os import name, system
from time import sleep

#Classes
class View (IView, IViewSubject):
    """Gerencia a tela de batalha"""
    def __init__(self) -> None:
        self.observers: list[IViewSubscriber] = []


    def subscribe(self, subscriber: IViewSubscriber) -> None:
        self.observers.append(subscriber)
    

    def unsubscribe(self, subscriber: IViewSubscriber) -> None:
        self.observers.remove(subscriber)


    def get_input_notify(self, escolha: Escolhas) -> None:
        for observer in self.observers:
            observer.get_input_update(escolha)

    
    def get_input(self, check: list[int] | None = None) -> Escolha:
        while True:
            escolha = input()
            
            try:
                escolha = Escolha(escolha)
                valor = escolha.getValue()
            except:
                print('Escolha inválida, por favor digite apenas números!')
                continue

            if check == None:
                return escolha

            if valor < 0 or valor >= check.__len__():
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