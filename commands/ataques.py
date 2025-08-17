#Commands de ataques
#Libs
from time import sleep
from configuracoes import Combate, Cores, ConfiguracaoBasicaAtaque, ConfiguracaoInvocacao
from typing import TYPE_CHECKING
from factorys import FactoryCriatura


if TYPE_CHECKING:
    from models import Criatura

#Classes Abstratas
class Command:
    """Command abstrato de ataque."""
    def __init__(self, rolagem: int | None = None) -> None:
        self.rolagem = rolagem


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


class CommandInvocarCriatura(Command):
    """Comando que executa a ação de invocar alguma criatura.
    """
    def __init__(self, criatura: str, lista_criaturas: list['Criatura'], rolagem: int, cfg: ConfiguracaoInvocacao) -> None:
        """    
        Args:
            criatura: Nome da criatura em formato de string.
            lista_criaturas: Lista da batalha que a criatura deverá ser adicionada.
            rolagem: Qual foi o valor tirado na rolagem de dados do usuário do command.
            cfg: Configuração Especifica da criatura para realizar invocações.
        """

        super().__init__()
        self.criatura = criatura
        self.lista_criatura = lista_criaturas
        self.rolagem = rolagem
        self.cfg = cfg
        self.factory = FactoryCriatura()

    
    def executar(self) -> None:
        print(id(self.lista_criatura))
        print(self.cfg.MENSAGENS.MENSAGEM_INICIO)
        self.contagem_regressiva(3)
        quantidade_invocacoes: int

        if self.rolagem == Combate.FALHA:
            print(self.cfg.MENSAGENS.MENSAGEM_FALHA)
            return
        
        if self.rolagem == Combate.CRITICO:
            quantidade_invocacoes = self.cfg.QUANTIDADE_INVOCACOES_CRITICO
            print(f'{quantidade_invocacoes}', self.cfg.MENSAGENS.MENSAGEM_CRITICO)
            
        else:
            quantidade_invocacoes = self.cfg.QUANTIDADE_INVOCACOES
            print(f'{quantidade_invocacoes}',self.cfg.MENSAGENS.MENSAGEM_NORMAL)
            

        for _ in range(0, quantidade_invocacoes):
                criatura = self.factory.criar_criatura(self.criatura)
                self.lista_criatura.append(criatura)
