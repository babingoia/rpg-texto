# Classe base para instância de batalha
#Libs
from __future__ import annotations
from os import system, name
from typing import TYPE_CHECKING, Union
from commands import Command

if TYPE_CHECKING:
    from models import Jogador, Criatura  

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
        print(id(self.inimigos))

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
        if name == 'nt':
            system("cls")
        else:
            system("clear")

    
    def checar_morte(self):
        """Verifica se algum inimigo morreu e remove ele do combate."""
        inimigos_vivos: list[Criatura] = []
        jogadores_vivos: list[Criatura] = []

        for inimigo in self.inimigos:
            if inimigo.vida > 0:
                inimigos_vivos.append(inimigo)
            else:
                print(f"{inimigo.nome} foi destruido!")

        for jogador in self.jogadores:
            if jogador.vida > 0:
                jogadores_vivos.append(jogador)
            else:
                print(f"{jogador.nome} foi destruido!")

        self.criaturas['inimigos'] = list(inimigos_vivos)
        self.criaturas['jogadores'] = list(jogadores_vivos)

        self.inimigos = self.criaturas['inimigos']
        self.jogadores = self.criaturas['jogadores']

        print("Inimigos:", self.inimigos)
        print("criaturas:", self.criaturas['inimigos'])


    def colocar_em_batalha(self) -> None:
        #Adiciona essa instancia de batalha a todas as criaturas envolvidas
        for lista_criaturas in self.criaturas.values():
            for criatura in lista_criaturas:
                criatura.batalha = self

    def iniciar(self) -> Union[list[Criatura], list[Jogador]]:
        """Inicia o loop de Batalha
        
        Returns:
            Criatura: Retorna quem venceu a batalha.
        """
        self.colocar_em_batalha()
        #Começa o loop de batalha
        while len(self.jogadores) > 0 and len(self.inimigos) > 0:
            for lista_criaturas in self.criaturas.values():
                for criatura in lista_criaturas:
                    
                    self.mostrar_stats_globais()
                    comandos: list[Command] = criatura.turno()

                    for comando in comandos:
                        comando.executar()

                    self.checar_morte()
                    self.colocar_em_batalha()

                    input("Aperte ENTER para continuar...")
                    self.limpar_tela()
            
        if len(self.inimigos) > 0:
            return self.inimigos
        else:
            return self.jogadores
