#Classe que cria alguma criatura.

#libs
from ..configuracoes.outras_configs import ConfigFactoryCriarCriaturas
from interfaces import ICriatura, ICriaturaFactory

cfg = ConfigFactoryCriarCriaturas()

class FactoryCriatura(ICriaturaFactory):
    """Classe estática que cria instâncias de criaturas."""
    @staticmethod
    def criar(tipo: str) -> ICriatura:
        """Método que cria uma instância de alguma criatura.
        
        Args:
        criatura: String com o nome da criatura a ser criada.
        """
        from models import Lich, Esqueleto, Clerigo, Paladino, Assassino
        
        match tipo:
            
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
