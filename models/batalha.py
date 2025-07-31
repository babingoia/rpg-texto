# Classe base para instância de batalha
#Libs
from __future__ import annotations
from os import system
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .Criatura import Criatura
    from .Jogadores.jogador import Jogador

#Classes
class Batalha:
    """Classe que gerencia as batalhas.
        -> Necessita uma configuração inicial de criaturas.
    """
    def __init__(self, inimigos: list[Criatura], jogadores: list[Criatura]) -> None:
        """Faz a criação de uma instância de batalha.
            
        Args:
            inimigos: Lista de inimigos dentro da batalha.
            jogadores: Lista de jogadores dentro da batalha.
        """
        self.criaturas: dict[str, list[Criatura]] = {
            "jogadores": jogadores,
            "inimigos": inimigos
        }
        self.jogadores = self.criaturas["jogadores"]
        self.inimigos = self.criaturas["inimigos"]

    def mostrar_stats_globais(self) -> None:
        """Mostra os status de todas as criaturas envolvidas na batalha."""
        
        print("Inimigos:")
        for inimigo in self.inimigos:
            inimigo.mostrar_stats()
        print()

        
        print("Jogadores:")
        for jogador in self.jogadores:
            jogador.mostrar_stats()
        print()

        
    def limpar_tela(self) -> None:
        """Limpa a tela do CMD"""
        system("cls")


    def iniciar(self) -> Union[list[Criatura], list[Jogador]]:
        """Inicia o loop de Batalha
        
        Returns:
            Criatura: Retorna quem venceu a batalha.
        """
        #Adiciona essa instancia de batalha a todas as criaturas envolvidas
        for lista_criaturas in self.criaturas.values():
            for criatura in lista_criaturas:
                criatura.batalha = self

        #Começa o loop de batalha
        while len(self.jogadores) > 0 and len(self.inimigos) > 0:
            for key, lista_criaturas in self.criaturas.items():
                for id, criatura in enumerate(lista_criaturas):
                    if criatura.vida <= 0:
                        print(f"Criatura: {criatura.nome} foi derrotada e não ataca.")
                        del self.criaturas[key][id]
                        continue
                
                    self.mostrar_stats_globais()
                    criatura.turno()
                    input("Aperte ENTER para continuar...")
                    self.limpar_tela()
            
        if len(self.inimigos) > 0:
            return self.inimigos
        else:
            return self.jogadores

