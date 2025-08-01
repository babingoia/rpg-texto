#Lógica para funcionamento do Lich
#Libs
from ..Criatura import Criatura
from ..Jogadores.jogador import Jogador
from typing import Union, Callable


#Classes
class Esqueleto(Criatura):
    """Classe específica para criar um esqueleto."""
    def __init__(self) -> None:
        """Cria uma instância de esqueleto com as características básicas."""
        super().__init__()
        self.nome = "esqueleto"
        self.vida = 10
        self.acoes: dict[int, Callable[[], Union[int, None]]] = {
            1: self.atacar
        }

    def mostrar_stats(self):
        """Mostra os status do esqueleto."""
        print('Vida do Esqueleto: {}'.format(self.vida))
        print()


    def atacar(self) -> int:
        """Lógica para um ataque básico de espada."""
        print('\nO esqueleto corre em sua direção com a espada levantada...')
        self.contagem_regressiva(3)
        atkL = self.rolar_dados(6, 1)
        if atkL == 1:
            print('\nVocê consegue desviar do ataque a tempo!')
            return 0
        elif atkL == 6:
            print('\nELE TE ACERTA EM CHEIO!!!\n[[Causou 8 de dano]]')
            return 8
        else:
            print('\nEle te corta.\n[[Causou 4 de dano]]')
            return 4


    def turno(self) -> Union[int, None]:
        """Lógica do turno de um esqueleto comum."""
        if self.batalha == None:
            return
        alvo = next((i for i,a in enumerate(self.batalha.jogadores) if isinstance(a, Jogador)), None)
        if alvo == None:
            return
        
        valor = self.atacar()
        if valor != None: # type: ignore
            self.batalha.jogadores[alvo].vida -= valor
        
        return alvo


class Lich(Esqueleto):
    """Classe para controlar o Lich. Ele inicia com algumas características de um esqueleto básico."""
    def __init__(self) -> None:
        """Inicia características próprias, o resto é a da classe base Esqueleto."""
        super().__init__()
        self.nome = "lich"
        self.vida = 100

    def mostrar_stats(self):
        """Mostra os status do Lich."""
        print('Vida do Lich: {}'.format(self.vida))
        print()


    #Ações
    def invocar_esqueleto(self) -> Union[int, None]:
        """Invoca um esqueleto e o adiciona a instância da batalha atual."""
        if self.batalha == None:
            return
        print('\nO Lich toca na terra, fazendo-a tremer...')
        self.contagem_regressiva(3)
        atkL = self.rolar_dados(6, 1)
        if atkL == 1:
            print('\nNada acontece')
        elif atkL == 6:
            print('\nDois esqueletos surgem da terra!')
            esqueleto1 = Esqueleto()
            esqueleto2 = Esqueleto()
            esqueleto1.batalha = self.batalha
            esqueleto2.batalha = self.batalha
            self.batalha.inimigos.append(esqueleto1)
            self.batalha.inimigos.append(esqueleto2)
        else:
            print('\nUm esqueleto surge da terra.')
            esqueleto = Esqueleto()
            esqueleto.batalha = self.batalha
            self.batalha.inimigos.append(esqueleto)


    def atacar(self) -> int:
        """Lógica para um ataque básico do Lich."""
        print('\nO Lich levanta suas mãos, invocando um raio necromante...')
        self.contagem_regressiva(3)
        atkL = self.rolar_dados(6, 1)
        if atkL == 1:
            print('\nVocê consegue desviar da magia a tempo!')
            return 0
        elif atkL == 6:
            print('\nELE TE ACERTA EM CHEIO!!!\n[[Causou 20 de dano]]')
            return 20
        else:
            print('\nEle acerta o raio em você.\n[[Causou 10 de dano]]')
            return 10


    def escolher_acao(self) -> Union[int, None]:
        """Função que escolhe aleatóriamente qual será a ação do lich em batalha."""
        escolha = self.rolar_dados(2,1)

        match escolha:
            case 1:
                self.invocar_esqueleto()
            case 2:
                valor = self.atacar()
                return valor
            case _:
                pass


    def turno(self) -> Union[int, None]:
        """Lógica de um turno do Lich em combate."""
        if self.batalha == None:
            return
        alvo = next((i for i,a in enumerate(self.batalha.jogadores) if isinstance(a, Jogador)), None)
        if alvo == None:
            return
        
        valor = self.escolher_acao()
        if valor != None: # type: ignore
            self.batalha.jogadores[alvo].vida -= valor
        
        return alvo