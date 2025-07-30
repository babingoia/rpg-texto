#Libs
from .Criatura import Criatura
from .Jogador import Jogador
from typing import Union, Callable

class Esqueleto(Criatura):
    def __init__(self) -> None:
        self.nome = "esqueleto"
        self.vida = 10
        self.acoes: dict[int, Callable[[], Union[int, None]]] = {
            1: self.atacar
        }

    def mostrar_stats(self):
        print('Vida do Esqueleto: {}'.format(self.vida))
        print()


    def atacar(self) -> int:
        print('\nO esqueleto corre em sua direção com a espada levantada...')
        self.contagem_regressiva(3)
        atkL = self.rolarD6(1)
        if atkL == 1:
            print('\nVocê consegue desviar do ataque a tempo!')
            return 0
        elif atkL == 6:
            print('\nELE TE ACERTA EM CHEIO!!!\n[[Causou 10 de dano]]')
            return 10
        else:
            print('\nEle te corta.\n[[Causou 5 de dano]]')
            return 5


    def turno(self) -> Union[int, None]:
        if self.batalha == None:
            return
        alvo = next((i for i,a in enumerate(self.batalha.criaturas) if isinstance(a, Jogador)), None)
        if alvo == None:
            return
        
        valor = self.atacar()
        if valor != None: # type: ignore
            self.batalha.criaturas[alvo].vida -= valor
        
        return alvo


class Lich(Esqueleto):
    def __init__(self) -> None:
        self.nome = "lich"
        self.vida = 100

    def mostrar_stats(self):
        print('Vida do Lich: {}'.format(self.vida))
        print()


    #Ações
    def invocar_esqueleto(self) -> Union[int, None]:
        if self.batalha == None:
            return
        print('\nO Lich toca na terra, fazendo-a tremer...')
        self.contagem_regressiva(3)
        atkL = self.rolarD6(1)
        if atkL == 1:
            print('\nNada acontece')
        elif atkL == 6:
            print('\nDois esqueletos surgem da terra!')
            esqueleto1 = Esqueleto()
            esqueleto2 = Esqueleto()
            esqueleto1.batalha = self.batalha
            esqueleto2.batalha = self.batalha
            self.batalha.criaturas.append(esqueleto1)
            self.batalha.criaturas.append(esqueleto2)
        else:
            print('\nUm esqueleto surge da terra.')
            esqueleto = Esqueleto()
            esqueleto.batalha = self.batalha
            self.batalha.criaturas.append(esqueleto)


    def atacar(self) -> int:
        print('\nO Lich levanta suas mãos, invocando um raio necromante...')
        self.contagem_regressiva(3)
        atkL = self.rolarD6(1)
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
        escolha = self.rolarD2(1)

        match escolha:
            case 1:
                self.invocar_esqueleto()
            case 2:
                valor = self.atacar()
                return valor
            case _:
                pass


    def turno(self) -> Union[int, None]:
        if self.batalha == None:
            return
        alvo = next((i for i,a in enumerate(self.batalha.criaturas) if isinstance(a, Jogador)), None)
        if alvo == None:
            return
        
        valor = self.escolher_acao()
        if valor != None: # type: ignore
            self.batalha.criaturas[alvo].vida -= valor
        
        return alvo