#Comando de invocar criaturas.
#Libs
from interfaces import ICriatura
from ..base import CommandBase
from typing import Union
from models import FactoryCriatura
from game_data import Combate

#Comando
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

