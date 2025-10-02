#Comando de modificar atributo.
#Libs
from typing import Any
from interfaces import ICriatura
from ..base.command_base import CommandBase

#Comando
class CommandRecuperarAtributo(CommandBase):
    def __init__(self,
                nome: str,
                rolagem: int,
                config: dict[str, Any],
                alvo: list[ICriatura] | None = None,
                ) -> None:
        super().__init__(nome, rolagem, config, alvo)


    def executar(self) -> dict[str, str | int]:
        
        if self.alvo == None:
            raise ValueError("Alvo inválido.")
        
        CONJURADOR = self.alvo[0]

        CONJURADOR.set_atributos(self.config['atributo_recuperado'], self.config['valor_recuperado'])
        
        data: dict[str, str | int] = {
            'acao': self.nome,
            'atributo_recuperado': self.config['atributo'],
            'valor_recuperado': self.config['valor_cura'],
            'alvo': CONJURADOR.get_nome(),
        }

        return data