#Lógica para funcionamento do Lich
#Libs
from typing import Callable
from ...configuracoes.criaturas.configurações_inimigos import LICH, ESQUELETO 
from commands import CommandAtaqueBasico, CommandInvocarCriatura
from interfaces import ICommand, ICriatura
from ..base import CriaturaBase


#Classes
class Esqueleto(CriaturaBase):
    """Classe específica para criar um esqueleto."""
    def __init__(self, config: ESQUELETO = ESQUELETO()) -> None:
        """Cria uma instância de esqueleto com as características básicas."""
        super().__init__(config.NOME, config.ATRIBUTOS)
        self.config = config
        self.acoes: dict[int, Callable[[ICriatura], list[ICommand]]] = {
            int(config.ATAQUES['ataque_basico']['id']): lambda alvo: self.atacar(alvo)
        }


    def atacar(self, alvo: ICriatura) -> list[ICommand]:
        """Lógica para um ataque básico de espada."""
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)

        comandos: list[ICommand] = [CommandAtaqueBasico(ESQUELETO.ATAQUE_BASICO, alvo, rolagem)]
        return comandos


class Lich(Esqueleto):
    """Classe para controlar o Lich. Ele inicia com algumas características de um esqueleto básico."""
    def __init__(self) -> None:
        """Inicia características próprias, o resto é a da classe base Esqueleto."""
        super().__init__()
        self.cfg = LICH
        self.nome = self.cfg.STATUS.NOME
        self.vida = self.cfg.STATUS.VIDA
        

    #Ações
    def invocar_esqueleto(self) -> list[Command]:
        """Invoca um esqueleto e o adiciona a instância da batalha atual."""
        
        if self.batalha == None:
            raise ValueError("Ops, não está em batalha!")
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        print(id(self.batalha.inimigos))
        comandos: list[Command] = [CommandInvocarCriatura('esqueleto', self.batalha.inimigos, rolagem, LICH.INVOCAR_ESQUELETO)]

        return comandos
    

    def atacar(self, alvo: ICriatura) -> list[ICommand]:
        """Lógica para um ataque básico de espada."""
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)

        comandos: list[ICommand] = [CommandAtaqueBasico(LICH.ATAQUE_BASICO, alvo, rolagem)]
        return comandos

