from __future__ import annotations
from os import system
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Criatura import Criatura

class Batalha:
    def __init__(self, criaturas: list[Criatura]) -> None:
        self.criaturas = criaturas
    

    def mostrar_stats_globais(self) -> None:
        for criatura in self.criaturas:
            criatura.mostrar_stats()

        
    def limpar_tela(self) -> None:
        system("cls")


    def iniciar(self) -> Criatura:
        while len(self.criaturas) > 1:
            for criatura in self.criaturas:
                criatura.batalha = self

            for id, criatura in enumerate(self.criaturas):
                if criatura.vida <= 0:
                    print(f"Criatura: {criatura.nome} foi derrotada e não ataca.")
                    del self.criaturas[id]
                    continue
                
                self.mostrar_stats_globais()
                criatura.turno()
                self.limpar_tela()
            
        return self.criaturas[0] #Só sobra uma então ela vai estar no 0                   

