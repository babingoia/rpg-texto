#Interfaces do sistema.
#libs
from abc import ABC, abstractmethod
from typing import Callable, Any, Optional

#Interface
class IAtaqueStrategy(ABC):
    @abstractmethod
    def escolher_alvo(self, alvos: dict[str, list['ICriatura']]) -> 'ICriatura': pass


class ICommand(ABC):
    @abstractmethod
    def executar(self) -> list['IData']: pass


class IData(ABC):
    @abstractmethod
    def get_data(self) -> dict[Any, Any]: pass

    @abstractmethod
    def add(self, chave: Any, valor: Any) -> None: pass

    @abstractmethod
    def remove(self, chave: Any, valor: Any) -> None: pass

    @abstractmethod
    def update(self, dados: dict[Any, Any]) -> None: pass


class ICriatura(ABC):
    @abstractmethod
    def get_atributos(self) -> dict[str, int]: pass

    @abstractmethod
    def get_nome(self) -> str: pass

    @abstractmethod
    def set_atributos(self, atributo: str, valor: int) -> None: pass

    @abstractmethod
    def get_acoes(self) -> dict[int, Callable[['ICriatura'], list[ICommand]]]: pass

    @abstractmethod
    def executar_acao(self, acao: int, alvo: Optional['ICriatura']) -> list[ICommand]: pass


class IBatalha(ABC):
    @abstractmethod
    def iniciar (self) -> str: pass

    @abstractmethod
    def get_inimigos(self) -> list[ICriatura]: pass

    @abstractmethod
    def get_jogadores(self) -> list[ICriatura]: pass


class IView(ABC):
    @abstractmethod
    def mostrar(self, dados: IData) -> None: pass

    @abstractmethod
    def get_input(self, check: list[int] | None = None) -> int: pass

    @abstractmethod
    def limpar_tela(self) -> None: pass


class IViewFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar(tipo: str) -> IView: pass


class IDataFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar(tipo: str, dados: dict[Any, Any]={}) -> IData: pass


class IAtaqueStrategyFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar(tipo: str, **kwargs: Any) -> IAtaqueStrategy: pass


class ICriaturaFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar(tipo: str) -> ICriatura: pass