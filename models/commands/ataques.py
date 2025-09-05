#Commands de ataques
#Libs
from interfaces import ICommand, ICriatura
from ..configuracoes.outras_configs import Combate
from ..factorys import FactoryCriatura
from typing import Any, Union

#Classes
class CommandBase(ICommand):
    def __init__(self, nome: str, rolagem: int, config: dict[str, Any], alvo: ICriatura | None = None) -> None:
        self.nome = nome
        self.rolagem = rolagem
        self.config = config
        self.alvo = alvo
    
    
    def executar(self) -> dict[str, Union[str, int]]:
        raise NotImplementedError


class CommandAtaqueBasico(CommandBase):
    """Ataque básico."""
    def __init__(self, rolagem: int, config: dict[str,Union[str, int]], alvo: ICriatura) -> None:
        super().__init__('ataque_basico', rolagem, config, alvo)


    def executar(self) -> dict[str, Union[str, int]]:
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
        
        acao: dict[str, Union[str, int]] = {
            'ataque': self.nome,
            'dano': dano,
            'rolagem': self.rolagem,
        }

        return acao


class CommandInvocarCriatura(CommandBase):
    """Comando que executa a ação de invocar alguma criatura.
    """
    def __init__(self, criatura: str, rolagem: int, config: dict[str,Union[str, int]], lista_criaturas: list[ICriatura]) -> None:
        """    
        Args:
            criatura: Nome da criatura em formato de string.
            lista_criaturas: Lista da batalha que a criatura deverá ser adicionada.
            rolagem: Qual foi o valor tirado na rolagem de dados do usuário do command.
            cfg: Configuração Especifica da criatura para realizar invocações.
        """

        super().__init__('invocar_criatura', rolagem, config)
        self.criatura = criatura
        self.lista_criatura = lista_criaturas
        self.rolagem = rolagem
        self.factory = FactoryCriatura()

    
    def executar(self) -> dict[str, Union[str, int]]:
        quantidade_invocacoes: int

        if self.rolagem == Combate.FALHA:
            quantidade_invocacoes = 0
        
        if self.rolagem == Combate.CRITICO:
            quantidade_invocacoes = self.config['quantidade_invocacoes'] * self.config['multiplicador_critico']
            
        else:
            quantidade_invocacoes = self.config['quantidade_invocacoes']
            

        for _ in range(0, quantidade_invocacoes):
                criatura = self.factory.criar(self.criatura)
                self.lista_criatura.append(criatura)
        
        dados: dict[str, Union[str, int]] = {
            'ataque': self.nome,
            'tipo_criatura_invocada': self.criatura,
            'rolagem': self.rolagem,
            'quantidade_criaturas_invocadas': quantidade_invocacoes
        }

        return dados
