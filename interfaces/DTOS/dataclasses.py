#Dataclasses do projeto.
#Libs
from dataclasses import dataclass
from typing import Union

#Dataclasses
@dataclass
class Escolha():
    def __init__(self, escolha: Union[str, int] ) -> None:
        
        escolha = self.validar(escolha)
        
        self.escolha: int = escolha
    

    def validar(self, escolha: Union[str, int]) -> int:
        if isinstance(escolha, str):
            escolha = escolha.strip()

            if escolha.isdigit() == False:
                print('Ops, sua escolha não contem apenas números!')

            escolha = int(escolha)

        return escolha
    

    def checar_intervalo(self, minimo: int, maximo: int) -> bool:
        if self.escolha < minimo or self.escolha > maximo:
            return False
        
        return True
    

    def getValue(self) -> int:
        return self.escolha
