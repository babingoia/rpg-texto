#Implementações concretas de estruturas de dados.
#Libs
from typing import TypedDict, Union, Callable, TYPE_CHECKING
from .dataclasses import Escolha

if TYPE_CHECKING:
    from ..interfaces import ICriatura, ICommand

#SubClasses
class Escolhas(TypedDict):
    acao_escolhida: Escolha
    alvo_selecionado: Union[list['ICriatura'], None]


class BatalhaData(TypedDict):
    """Dicionário tipado. Armazena informações importantes para uma batalha."""
    inimigos: list['ICriatura']
    jogadores: list['ICriatura']
    ordem_turnos: list['ICriatura']


class BatalhaInicioTurno(TypedDict):
    """Dicionário tipado. Contém informações do inicio de turno da batalha."""
    criaturas: BatalhaData
    criatura_atual: 'ICriatura'
    acoes_disponiveis: dict[int, Callable[['list[ICriatura] | None'], list['ICommand']]]


class BatalhaFinalTurno(TypedDict):
    criaturas: BatalhaData
    criatura_atual: 'ICriatura'
    acoes_executadas: list[dict[str, Union[str, int]]]


class BatalhaFinal(TypedDict):
    criaturas: list['ICriatura']


class Mensagem(TypedDict):
    """Dicionário tipado. Padrão de mensagem que a view lê."""
    mensagem: dict[str, str]


class ViewData(TypedDict):
    """Dicionario tipado. Armazena algo que a view consegue ler."""
    cor: str
    titulo: str
    mensagens: list[dict[str, str]]


class AtributosBase(TypedDict):
    """Dicionário tipado.
    
    Keys: \n
    vida_maxima: int \n
    vida_atual: int \n

    """
    vida_maxima: int
    vida_atual: int


class AtributosMagicos(AtributosBase):
    """Dicionário tipado, extensão de atributos base.
    
    Keys:\n
    vida_maxima: int \n
    vida_atual: int \n
    mana_maxima: int \n
    mana_atual: int \n
    restauracao_mana_critico: int \n
    
    """
    mana_maxima: int
    mana_atual: int
    restauracao_mana_critico: int