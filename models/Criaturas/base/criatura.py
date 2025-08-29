#Classe base para criaturas
#libs
from interfaces import ICommand, ICriatura
from typing import Callable, Optional
from random import randint

#classes
class CriaturaBase(ICriatura):
    def __init__(self, nome: str, atributos: dict[str, int]) -> None:
        self.nome: str = nome
        self.atributos = atributos
        self.acoes: dict[int, Callable[[ICriatura], list[ICommand]]]
    

    def get_nome(self) -> str:
        return self.nome
    

    def get_atributos(self) -> dict[str, int]:
        return self.atributos
    
    
    def set_atributos(self, atributo: str, valor: int) -> None:
        self.atributos[atributo] += valor

    
    def get_acoes(self) -> dict[int, Callable[[ICriatura], list[ICommand]]]:
        return self.acoes


    def executar_acao(self, acao: int, alvo: Optional[ICriatura]) -> list[ICommand]:
        raise NotImplementedError('Funcao de executar acao nao implementada para essa criatura!')
    

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
