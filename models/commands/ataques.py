#Commands de ataques
#Libs
from interfaces import ICommand, ICriatura
from configuracoes import Combate
from factorys import FactoryCriatura


#Classes
class CommandBase(ICommand):
    def __init__(self, nome: str, rolagem: int, config: dict[str,int], alvo: ICriatura | None = None) -> None:
        self.nome = nome
        self.rolagem = rolagem
        self.config = config
        self.alvo = alvo
    
    
    def executar(self) -> None:
        raise NotImplementedError


class CommandAtaqueBasico(CommandBase):
    """Ataque básico."""
    def __init__(self, nome: str, rolagem: int, config: dict[str,int], alvo: ICriatura) -> None:
        super().__init__(nome, rolagem, config, alvo)


    def executar(self) -> None:
        if self.alvo == None:
            raise ValueError("Alvo não encontrado!")
        
        dano: int = 0

        if self.rolagem == Combate.FALHA:
            dano = Combate.DANO_FALHA
            
        elif self.rolagem == Combate.CRITICO:
            dano = self.config['dano'] * self.config['multiplicador_critico']
            
        else:
            dano = self.config['dano']
        
        self.alvo.set_atributos('vida_atual', -1*dano)


class CommandInvocarCriatura(CommandBase):
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
