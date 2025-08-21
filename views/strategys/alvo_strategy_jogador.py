#Classe base para um jogador.
#libs
from interfaces import IAlvoStrategy, ICriatura


#Classes
class Jogador(IAlvoStrategy):
    
    def escolher_alvo(self, alvos: list[ICriatura]) -> ICriatura:
        
        print("Escolha um alvo:")
        for index, alvo in enumerate(alvos):
            print(f"{index} = {alvo.get_nome()}")
        
        while True:
            alvo = input()

            if not alvo.isdigit():
                print("Alvo inválido, tente novamente.")
                continue
            
            alvo = int(alvo)

            if not (0 <= alvo < len(alvos)):
                print("Alvo inválido, tente novamente.")
                continue

            return alvos[alvo]
