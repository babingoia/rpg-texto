#Bibliote de efeitos
#libs
from .base import Command
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Criatura


#Classe Abstrata
class CommandRecuperarVida(Command):
    """Cura o alvo no valor da rolagem."""
    def __init__(self, rolagem: int, alvo: 'Criatura') -> None:
        """
        Args:
        rolagem: Valor de vida a ser recuperado.
        alvo: criatura que terá a vida restaurada.
        """
        super().__init__(rolagem)
        self.alvo = alvo


    def executar(self) -> None:
        self.alvo.vida = min(self.rolagem + self.alvo.vida, self.alvo.vida_maxima)


class CommandRecuperarMana(Command):
    """Cura o alvo no valor da rolagem."""
    def __init__(self, rolagem: int, alvo: 'Criatura') -> None:
        """
        Args:
        rolagem: Valor de mana a ser recuperado.
        alvo: criatura que terá a mana restaurada.
        """
        super().__init__(rolagem)
        self.alvo = alvo


    def executar(self) -> None:
        self.alvo.mana = min(self.rolagem + self.alvo.mana, self.alvo.mana_maxima)
