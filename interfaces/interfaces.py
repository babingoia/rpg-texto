#Interfaces do sistema.
#libs
from abc import ABC, abstractmethod
from time import sleep
from random import randint
from typing import Callable


#Interfaces
class ICommand(ABC):
    @abstractmethod
    def executar(self) -> None: pass

    def contagem_regressiva(self, segundos: int) -> None:
        """Inicia uma contagem regressiva.
        
        Args:
            segundos: quantidade de segundos que a contagem vai demorar.
        """
        for i in range(segundos, 0, -1):
            print(f"{i}...", end=' ', flush=True)
            sleep(1)
        print('\n')


class ICriatura(ABC):
    @abstractmethod
    def get_acoes(self) -> dict[int, Callable[['ICriatura'], list[ICommand]]]: pass

    @abstractmethod
    def get_atributos(self) -> dict[str, int]: pass

    @abstractmethod
    def get_nome(self) -> str: pass

    @abstractmethod
    def set_atributos(self, atributo: str, valor: int) -> None: pass

    def rolar_dados(self, dado: int, n_dados: int, valor: int = 0) -> int:
        """Rola um dado de x lados x vezes.
        
        Args:
            dado: Quantidade de lados do dado a ser rolado.
            n_dados: Quantidade de dados a serem rolados.
            valor: É o número inicial sem nenhuma rolagem de dados, pode ser usado para atribuir um bônus inicial. Valor padrão 0.
        """
        valor += randint(1,dado)
        
        n_dados -= 1
        
        if n_dados > 0:
            return self.rolar_dados(dado, n_dados, valor) #Loop recursivo.

        return valor    


class IAlvoStrategy(ABC):
    @abstractmethod
    def escolher_alvo(self, alvos: list[ICriatura]) -> ICriatura: pass


class IBatalha(ABC):
    @abstractmethod
    def iniciar (self) -> None: pass

    @abstractmethod
    def get_inimigos(self) -> list[ICriatura]: pass

    @abstractmethod
    def get_jogadores(self) -> list[ICriatura]: pass