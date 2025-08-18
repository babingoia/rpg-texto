#Classe base abstrata de command
#libs
from time import sleep


#Classes
class Command:
    """Command abstrato de ataque."""
    def __init__(self, rolagem: int) -> None:
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
