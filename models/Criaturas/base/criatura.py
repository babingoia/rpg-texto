#Classe base para criaturas
#libs
from interfaces import ICommand, ICriatura, AtributosBase
from typing import Callable, Optional, Generic, TypeVar
from random import randint
from inspect import signature


A = TypeVar('A', bound=AtributosBase)


#classes
class CriaturaBase(ICriatura, Generic[A]):
    def __init__(self, nome: str, atributos: A) -> None:
        self.nome: str = nome
        self.atributos: A = atributos
        self.acoes: dict[int, Callable[[ICriatura | None], list[ICommand]]]
    

    def get_nome(self) -> str:
        return self.nome
    
    
    def get_atributos(self) -> A:
        return self.atributos
    

    def set_atributos(self, atributo: str, valor: int) -> None:
        self.atributos[atributo] += valor

    
    def get_acoes(self) -> dict[int, Callable[[ICriatura | None], list[ICommand]]]:
        return self.acoes


    def executar_acao(self, acao: int, alvo: Optional[ICriatura]) -> list[ICommand]:
        if 'alvo' in signature(self.acoes[acao]).parameters:
            if alvo is None:
                raise ValueError("Alvo não é válido.")
            comandos = self.acoes[acao](alvo)
            return comandos
        else:
            comandos = self.acoes[acao](alvo) # type: ignore nesse caso acoes nem de alvo
            return comandos
    

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
