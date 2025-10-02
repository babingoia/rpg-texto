#Classe base de um command.
#libs
from interfaces import ICriatura, ICommand
from typing import Union, Any

#Classe
class CommandBase(ICommand):
    def __init__(self, nome: str, rolagem: int, config: dict[str, Any], alvo: list[ICriatura] | None = None) -> None:
        self.nome = nome
        self.rolagem = rolagem
        self.config = config
        self.alvo = alvo
    
    
    def executar(self) -> dict[str, Union[str, int]]:
        raise NotImplementedError
