# Classe base de qualquer criatura
#livs
from __future__ import annotations
from typing import Union, TYPE_CHECKING, Callable
import random
import time
from .Configs.configs import Combate, ConfiguracaoBasicaAtaque
from .Ataques.Commands import Command, CommandAtaqueBasico

from models.Gerenciadores.batalha import Batalha
from .Ataques.Commands import Command
if TYPE_CHECKING:
    from Gerenciadores.batalha import Batalha


#classses
class Criatura:
    """Classe que possui os métodos e atributos básicos de uma criatura"""
    def __init__(self, batalha: Union[Batalha, None]=None) -> None:
        """Atributos básicos de uma criatura
        
        Args:
            Batalha: Pode carregar uma instância de batalha na criatura diretamente. Por padrão é None.
        """
        self.vida = 0
        self.mana = 0
        self.nome = None
        self.batalha: Union[Batalha, None] = batalha
        self.acoes_ataque: dict[int, Callable[[], list[Command]]] = {}
        self.acoes_buff: dict[int, Callable[[], None]] = {}



    def mostrar_stats(self) -> None:
        """Mostra os status da criatura."""
        print(f'\nVida do {self.nome}: {self.vida}')
        print(f"Mana do {self.nome}: {self.mana}")


    def contagem_regressiva(self, segundos: int) -> None:
        """Inicia uma contagem regressiva.
        
        Args:
            segundos: quantidade de segundos que a contagem vai demorar.
        """
        for i in range(segundos, 0, -1):
            print(f"{i}...", end=' ', flush=True)
            time.sleep(1)
        print('\n')


    def rolar_dados(self, dado: int, n_dados: int, valor: int = 0) -> int:
        """Rola um dado de x lados x vezes.
        
        Args:
            dado: Quantidade de lados do dado a ser rolado.
            n_dados: Quantidade de dados a serem rolados.
            valor: É o número inicial sem nenhuma rolagem de dados, pode ser usado para atribuir um bônus inicial. Valor padrão 0.
        """
        valor += random.randint(1,dado)
        
        n_dados -= 1
        
        if n_dados > 0:
            return self.rolar_dados(dado, n_dados, valor) #Loop recursivo.

        return valor    


    def ataque_basico(self, cfg_ataque_basico: ConfiguracaoBasicaAtaque) -> list[Command]:
        """Lógica para um ataque básico do Lich."""
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        alvo = self.escolher_alvo()

        comandos: list[Command] = [CommandAtaqueBasico(cfg_ataque_basico, alvo, rolagem)]
        return comandos    


    def escolher_alvo(self) -> "Criatura":
        raise NotImplementedError("Funcao de escolher alvo nao implementada.")


    def turno(self) -> list[Command]:
        """Executa a lógica de combate do turno da criatura. Deve ser implementado em toda subclasse para que o combate funcione adequadamente.
        """
        raise NotImplementedError