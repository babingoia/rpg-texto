#Lógica para funcionamento do Lich
#Libs
from ..Criatura import Criatura
from ..Jogadores.jogador import Jogador
from typing import Union, Callable
from configs import Dados, LICH, ESQUELETO, Combate


#Classes
class Esqueleto(Criatura):
    """Classe específica para criar um esqueleto."""
    def __init__(self) -> None:
        """Cria uma instância de esqueleto com as características básicas."""
        super().__init__()
        self.nome = ESQUELETO.NOME
        self.vida = ESQUELETO.VIDA
        self.acoes: dict[int, Callable[[], Union[int, None]]] = {
            ESQUELETO.ID_ATAQUE_BASICO: self.atacar
        }

    def mostrar_stats(self):
        """Mostra os status do esqueleto."""
        print('Vida do Esqueleto: {}'.format(self.vida))
        print()


    def atacar(self) -> int:
        """Lógica para um ataque básico de espada."""
        print('\nO esqueleto corre em sua direção com a espada levantada...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        atkL = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        dano = ESQUELETO.DANO_ATAQUE_BASICO
        
        if atkL == Combate.FALHA:
            print('\nVocê consegue desviar do ataque a tempo!')
            dano = Combate.DANO_FALHA
            return dano
        
        elif atkL == Combate.CRITICO:
            dano *= ESQUELETO.MULTIPLICADOR_CRITICO
            print('\nELE TE ACERTA EM CHEIO!!!\n[[Causou {dano} de dano]]')
            return dano
        
        else:
            print('\nEle te corta.\n[[Causou {} de dano]]')
            return dano


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
        self.nome = LICH.NOME
        self.vida = LICH.VIDA

    def mostrar_stats(self):
        """Mostra os status do Lich."""
        print('Vida do Lich: {}'.format(self.vida))
        print()


    #Ações
    def invocar_esqueleto(self) -> Union[int, None]:
        """Invoca um esqueleto e o adiciona a instância da batalha atual."""
        
        if self.batalha == None:
            return
        
        n_esqueletos = LICH.QUANTIDADE_ESQUELETOS_INVOCADOS

        print('\nO Lich toca na terra, fazendo-a tremer...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        atkL = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        
        if atkL == Combate.FALHA:
            print('\nNada acontece')
        
        elif atkL == Combate.CRITICO:

            n_esqueletos *= LICH.MULTIPLICADOR_CRITICO

            print(f'\n {n_esqueletos} esqueletos surgem da terra!')

            while n_esqueletos != 0:
                esqueleto = Esqueleto()
                
                esqueleto.batalha = self.batalha
                
                self.batalha.inimigos.append(esqueleto)

                n_esqueletos -= 1
                print(esqueleto.batalha, esqueleto.batalha.inimigos)
        
        else:
            print(f'\n {n_esqueletos} esqueleto surge da terra.')
            esqueleto = Esqueleto()
            esqueleto.batalha = self.batalha
            print(esqueleto.batalha)
            self.batalha.inimigos.append(esqueleto)
            print(esqueleto.batalha.inimigos)


    def atacar(self) -> int:
        """Lógica para um ataque básico do Lich."""

        print('\nO Lich levanta suas mãos, invocando um raio necromante...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        atkL = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        dano = LICH. DANO_ATAQUE_BASICO

        if atkL == Combate.FALHA:
            dano = Combate.DANO_FALHA
            print('\nVocê consegue desviar da magia a tempo!')
            return dano
        
        elif atkL == Combate.CRITICO:
            dano *= LICH.MULTIPLICADOR_CRITICO
            print(f'\nELE TE ACERTA EM CHEIO!!!\n[[Causou {dano} de dano]]')
            return dano
        
        else:
            print(f'\nEle acerta o raio em você.\n[[Causou {dano} de dano]]')
            return dano


    def escolher_acao(self) -> Union[int, None]:
        """Função que escolhe aleatóriamente qual será a ação do lich em batalha."""
        escolha = self.rolar_dados(Dados.D2,1)

        match escolha:
            case LICH.ID_INVOCAR_ESQUELETO:
                self.invocar_esqueleto()
            case LICH.ID_ATAQUE_BASICO:
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