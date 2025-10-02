#Lógica para funcionamento do Lich
#Libs
from typing import Callable
from ...configuracoes.criaturas.configurações_inimigos import LICH, ESQUELETO
from game_data import Combate
from ...commands.ataques import CommandAtaqueBasico, CommandInvocarCriatura
from interfaces import ICommand, ICriatura, AtributosBase
from ..base import CriaturaBase


#Classes
class Esqueleto(CriaturaBase[AtributosBase]):
    """Classe específica para criar um esqueleto."""
    def __init__(self, config: ESQUELETO = ESQUELETO()) -> None:
        """Cria uma instância de esqueleto com as características básicas."""
        super().__init__(config.nome, config.atributos)

        self.config = config
        
        self.acoes: dict[int, Callable[[list[ICriatura] | None], list[ICommand]]] = {
            int(config.ataques['ataque_basico']['id']): lambda alvo: self.atacar(alvo)
        }


    def atacar(self, alvo: list[ICriatura] | None) -> list[ICommand]:
        """Lógica para um ataque básico de espada."""
        if alvo == None:
            raise ValueError('Ops, alvo = None.')
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)

        comandos: list[ICommand] = [CommandAtaqueBasico(rolagem, self.config.ataques['ataque_basico'], alvo)]
        return comandos


class Lich(CriaturaBase[AtributosBase]):
    """Classe para controlar o Lich. Ele inicia com algumas características de um esqueleto básico."""
    def __init__(self, config: LICH = LICH()) -> None:
        """Inicia características próprias, o resto é a da classe base Esqueleto."""
        super().__init__(config.nome, config.atributos)
        
        self.config = config
        
        self.acoes = {
            # int(self.config.ataques['ataque_basico']['id']): lambda alvo: self.atacar(alvo),
            int(self.config.ataques['ataque_basico']['id']): lambda alvos: self.invocar_esqueleto(alvos)
        }
        

    #Ações
    def invocar_esqueleto(self, alvos: list[ICriatura] | None) -> list[ICommand]:
        """Invoca um esqueleto e o adiciona a instância da batalha atual."""
        if alvos == None:
            raise ValueError("Alvo inválido!")
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        comandos: list[ICommand] = [CommandInvocarCriatura('esqueleto', rolagem, self.config.ataques['invocar_esqueleto'], alvos)]

        return comandos
    

    def atacar(self, alvo: list[ICriatura] | None) -> list[ICommand]:
        """Lógica para um ataque básico de espada."""
        if alvo == None:
            raise ValueError("Ops, alvo = None.")
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)

        comandos: list[ICommand] = [CommandAtaqueBasico(rolagem, self.config.ataques['ataque_basico'], alvo)]
        return comandos

