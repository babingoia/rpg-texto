#Estratégia de seleção de alvo da IA.
#libs
from interfaces import ICriatura, IAlvoStrategy
from random import randint


#Strategy
class IA(IAlvoStrategy):

    def escolher_alvo(self, alvos: list[ICriatura]) -> ICriatura:

        dado = alvos.__len__() - 1

        alvo = alvos[randint(0, dado)]
        
        return alvo