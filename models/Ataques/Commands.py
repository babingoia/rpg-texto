#Commands de ataques
#Libs
from time import sleep
import random
from ..Configs.configsCriaturas import ConfiguracaoBasicaAtaque
from ..Configs.configs import Combate, Cores
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..Criatura import Criatura

#Classes Abstratas
class Command:
    """Command abstrato de ataque."""

    def executar(self) -> None:
        raise NotImplementedError
    

    def contagem_regressiva(self, segundos: int) -> None:
        """Inicia uma contagem regressiva.
        
        Args:
            segundos: quantidade de segundos que a contagem vai demorar.
        """
        for i in range(segundos, 0, -1):
            print(f"{i}...", end=' ', flush=True)
            sleep(1)
        print('\n')

    
    def rolar_dados(self, dado: int, n_dados: int, valor: int = 0) -> int:
        """Rola um dado de x lados x vezes.
        
        Args:
            dado: Quantidade de lados do dado a ser rolado.
            n_dados: Quantidade de dados a serem rolados.
            valor: É o número inicial sem nenhuma rolagem de dados, pode ser usado para atribuir um bônus inicial. Valor padrão 0.
        """
        valor += random.randint(1,dado)
        
        n_dados -= 1
        
        if n_dados > 0:
            return self.rolar_dados(dado, n_dados, valor) #Loop recursivo.

        return valor    


#Classes especificas
class CommandAtaqueBasico(Command):
    """Ataque básico."""
    def __init__(self, configurações: ConfiguracaoBasicaAtaque, alvo: "Criatura", rolagem: int) -> None:
        super().__init__()
        self.cfg = configurações
        self.alvo = alvo
        self.rolagem = rolagem

    def executar(self) -> None:
        print(self.cfg.MENSAGENS.MENSAGEM_INICIO)
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        dano: int = 0

        if self.rolagem == Combate.FALHA:
            dano = Combate.DANO_FALHA
            print(self.cfg.MENSAGENS.MENSAGEM_FALHA)
            
        elif self.rolagem == Combate.CRITICO:
            dano = self.cfg.DANO * self.cfg.MULTIPLICADOR_CRITICO
            print(self.cfg.MENSAGENS.MENSAGEM_CRITICO, f'[[Causou {dano} de dano]]{Cores.RESET}')
            
        else:
            dano = self.cfg.DANO
            print(self.cfg.MENSAGENS.MENSAGEM_NORMAL, f'[[Causou {dano} de dano]]')
            
        self.alvo.vida -= dano
