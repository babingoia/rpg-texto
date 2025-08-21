#Classe base para criaturas
#libs
from interfaces import ICriatura, ICommand
from typing import Callable


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
