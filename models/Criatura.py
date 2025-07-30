#livs
from __future__ import annotations
from typing import Union, TYPE_CHECKING
import random
import time

if TYPE_CHECKING:
    from .batalha import Batalha


#Consts
YELLOW = '\033[93m'
RESET = '\033[0m'


#classses
class Criatura:
    def __init__(self) -> None:
        self.vida = 0
        self.nome = None
        self.batalha: Union[Batalha, None] = None


    def mostrar_stats(self) -> None:
        pass


    def contagem_regressiva(self, segundos: int) -> None:
        for i in range(segundos, 0, -1):
            print(f"{i}...", end=' ', flush=True)
            time.sleep(1)
        print('\n')


    #Dados
    def rolarD2(self, n_dados: int, valor: int = 0):
                
        valor += random.randint(1,2)
        
        n_dados -= 1
        
        if n_dados > 0:
            return self.rolarD8(n_dados, valor)

        return valor    


    def rolarD6(self, n_dados: int, valor: int=0) -> int:
        
        valor += random.randint(1,6)
        
        n_dados -= 1
        
        if n_dados > 0:
            return self.rolarD8(n_dados, valor)

        return valor
    
    def rolarD8(self, n_dados: int, valor: int=0) -> int:
        
        valor += random.randint(1,8)
        
        n_dados -= 1
        
        if n_dados > 0:
            return self.rolarD8(n_dados, valor)

        return valor
    

    def turno(self) -> Union[int, None]:
        pass
