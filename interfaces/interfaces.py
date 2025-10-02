#Interfaces do sistema.
#libs
from abc import ABC, abstractmethod
from typing import Callable, Any, Optional, Union
from .DTOS import AtributosBase, BatalhaData, BatalhaInicioTurno, BatalhaFinalTurno, BatalhaFinal, Escolhas, Escolha

#Interface
class IViewSubscriber(ABC):
    @abstractmethod
    def get_input_update(self, escolhas: Escolhas) -> None: pass


class IBatalhaSubscriber(ABC):
    @abstractmethod
    def battle_start_update(self, data: BatalhaData) -> None: pass

    @abstractmethod
    def battle_end_update(self, data: BatalhaFinal) -> None: pass

    @abstractmethod
    def turn_start_update(self, data: BatalhaInicioTurno) -> None: pass

    @abstractmethod
    def turn_end_update(self, data: BatalhaFinalTurno) -> None: pass


class IViewSubject(ABC):
    @abstractmethod
    def subscribe(self, subscriber: IViewSubscriber) -> None: pass

    @abstractmethod
    def unsubscribe(self, subscriber: IViewSubscriber) -> None: pass

    @abstractmethod
    def get_input_notify(self, escolha: Escolhas) -> None: pass


class IBatalhaSubject(ABC):
    @abstractmethod
    def subscribe(self, subscriber: IBatalhaSubscriber) -> None: pass

    @abstractmethod
    def unsubscribe(self, subscriber: IBatalhaSubscriber) -> None: pass

    @abstractmethod
    def battle_start_notify(self, data: BatalhaData) -> None: pass

    @abstractmethod
    def battle_end_notify(self, data: BatalhaFinal) -> None: pass

    @abstractmethod
    def turn_start_notify(self, data: BatalhaInicioTurno) -> None: pass

    @abstractmethod
    def turn_end_notify(self, data: BatalhaFinalTurno) -> None: pass


class IAtaqueStrategy(ABC):
    @abstractmethod
    def get_escolhas(self, data: BatalhaInicioTurno) -> Escolhas: pass


class ICommand(ABC):
    @abstractmethod
    def executar(self) -> dict[str, Union[str, int]]: pass


class ICriatura(ABC):
    @abstractmethod
    def get_atributos(self) -> AtributosBase: pass

    @abstractmethod
    def get_nome(self) -> str: pass

    @abstractmethod
    def set_atributos(self, atributo: str, valor: int) -> None: pass

    @abstractmethod
    def get_acoes(self) -> dict[int, Callable[[ 'list[ICriatura] | None'], list[ICommand]]]: pass

    @abstractmethod
    def executar_acao(self, acao: int, alvo: Optional[list['ICriatura']]) -> list[ICommand]: pass


class IBatalha(ABC):
    @abstractmethod
    def iniciar (self) -> None: pass


class IView(ABC):
    @abstractmethod
    def get_input(self, check: list[int] | None = None) -> Escolha: pass

    @abstractmethod
    def limpar_tela(self) -> None: pass


class IViewFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar(tipo: str) -> IView: pass


class IAtaqueStrategyFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar(tipo: str, **kwargs: Any) -> IAtaqueStrategy: pass


class ICriaturaFactory(ABC):
    @staticmethod
    @abstractmethod
    def criar(tipo: str) -> ICriatura: pass