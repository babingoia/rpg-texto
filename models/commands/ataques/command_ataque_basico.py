#Comando de ataque basico
#Libs
from ..base.command_base import CommandBase
from typing import Union
from interfaces import ICriatura
from game_data import Combate


#Comando
class CommandAtaqueBasico(CommandBase):
    """Ataque básico."""
    def __init__(self, rolagem: int, config: dict[str,Union[str, int]], alvo: list[ICriatura]) -> None:
        super().__init__('ataque_basico', rolagem, config, alvo)


    def executar(self) -> dict[str, Union[str, int]]:
        if self.alvo == None:
            raise ValueError("Alvo não encontrado!")
        
        PRIMEIRO_ALVO: int = 0
        dano: int = 0

        if self.rolagem == Combate.FALHA:
            dano = Combate.DANO_FALHA
            
        elif self.rolagem == Combate.CRITICO:
            dano = self.config['dano'] * self.config['multiplicador_critico']
            
        else:
            dano = self.config['dano']
        
        self.alvo[PRIMEIRO_ALVO].set_atributos('vida_atual', -1*dano)
        
        acao: dict[str, Union[str, int]] = {
            'ataque': self.nome,
            'dano': dano,
            'rolagem': self.rolagem,
        }

        return acao