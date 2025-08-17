#Classe que cria alguma criatura.

#libs
from configuracoes import ConfigFactoryCriarCriaturas
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models import Criatura

cfg = ConfigFactoryCriarCriaturas()

class FactoryCriatura:
    """Classe estática que cria instâncias de criaturas."""
    @staticmethod
    def criar_criatura(criatura: str) -> 'Criatura':
        """Método que cria uma instância de alguma criatura.
        
        Args:
        criatura: String com o nome da criatura a ser criada.
        """
        from models import Lich, Esqueleto, Clerigo, Paladino, Assassino
        match criatura:
            
            case cfg.ESQUELETO:
                return Esqueleto()
            
            case cfg.LICH:
                return Lich()
            
            case cfg.PALADINO:
                return Paladino()
            
            case cfg.ASSASSINO:
                return Assassino()
            
            case cfg.CLERIGO:
                return Clerigo()
            
            case _:
                raise ValueError("Criatura não identificada para criação.")
