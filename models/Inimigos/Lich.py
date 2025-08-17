#Lógica para funcionamento do Lich
#Libs
from ..Jogadores.jogador import IA
from typing import Union, Callable
from ..Configs.configs import Dados, LICH, ESQUELETO, Combate
from ..Ataques.Commands import Command, CommandAtaqueBasico
from ..Gerenciadores.batalha import Batalha

#Classes
class Esqueleto(IA):
    """Classe específica para criar um esqueleto."""
    def __init__(self, batalha: Union[Batalha, None] = None) -> None:
        """Cria uma instância de esqueleto com as características básicas."""
        super().__init__()
        self.nome = ESQUELETO.STATUS.NOME
        self.vida = ESQUELETO.STATUS.VIDA
        self.acoes: dict[int, Callable[[], Union[int, list[Command]]]] = {
            ESQUELETO.ATAQUE_BASICO.ID: self.atacar
        }
        self.batalha = batalha

    def mostrar_stats(self):
        """Mostra os status do esqueleto."""
        print('Vida do Esqueleto: {}'.format(self.vida))
        print()


    def atacar(self) -> list[Command]:
        """Lógica para um ataque básico de espada."""
        alvo = self.escolher_alvo()
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)

        comandos: list[Command] = [CommandAtaqueBasico(ESQUELETO.ATAQUE_BASICO, alvo, rolagem)]
        return comandos


    def turno(self) -> list[Command]:
        """Lógica do turno de um esqueleto comum."""
        comandos = self.atacar()
        return comandos



class Lich(Esqueleto):
    """Classe para controlar o Lich. Ele inicia com algumas características de um esqueleto básico."""
    def __init__(self) -> None:
        """Inicia características próprias, o resto é a da classe base Esqueleto."""
        super().__init__()
        self.cfg = LICH
        self.nome = self.cfg.STATUS.NOME
        self.vida = self.cfg.STATUS.VIDA
        

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


    def escolher_acao(self) -> list[Command]:
        """Função que escolhe aleatóriamente qual será a ação do lich em batalha."""
        escolha = self.rolar_dados(Dados.D2,1)
        comandos: list[Command] = []
        match escolha:
            case LICH.ID_INVOCAR_ESQU:
                comandos = self.invocar_esqueleto()
            case LICH.ATAQUE_BASICO.ID:
                comandos = self.atacar()
            case _:
                pass

        return comandos


    def turno(self) -> list[Command]:
        """Lógica de um turno do Lich em combate."""
        
        comandos = self.atacar()
        
        return comandos