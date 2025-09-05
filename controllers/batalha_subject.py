#Classe base pora batalha subject
#Libs
from interfaces import IBatalhaSubject, IBatalhaSubscriber, BatalhaData, BatalhaFinal, BatalhaFinalTurno, BatalhaInicioTurno

#Classe
class BaseBatalhaSubject(IBatalhaSubject):
    def __init__(self) -> None:
        self.observers: list[IBatalhaSubscriber] = []
    

    def subscribe(self, subscriber: IBatalhaSubscriber) -> None:
        self.observers.append(subscriber)
    

    def unsubscribe(self, subscriber: IBatalhaSubscriber) -> None:
        if subscriber in self.observers:
            self.observers.remove(subscriber)


    def battle_start_notify(self, data: BatalhaData) -> None:
        for observer in self.observers:
            observer.battle_start_update(data)


    def battle_end_notify(self, data: BatalhaFinal) -> None:
        for observer in self.observers:
            observer.battle_end_update(data)


    def turn_start_notify(self, data: BatalhaInicioTurno) -> None:
        for observer in self.observers:
            observer.turn_start_update(data)
    

    def turn_end_notify(self, data: BatalhaFinalTurno) -> None:
        for observer in self.observers:
            observer.turn_end_update(data)