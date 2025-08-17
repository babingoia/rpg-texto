# Classe Paladino
#Libs
from ..Configs.configs import PALADINO, Combate,  Cores
from .jogador import Jogador
from typing import Union, Callable
from ..Ataques.Commands import Command, CommandAtaqueBasico


class Paladino(Jogador):
    """Classe especifica para criar um paladino."""
    def __init__(self):
        """Cria uma instância de paladino com suas características básicas."""
        super().__init__()
        self.nome = PALADINO.STATUS.NOME
        self.vida: int = PALADINO.STATUS.VIDA
        self.mana: int = PALADINO.STATUS_MAGO.MANA_MAXIMA

        #Esse distinção de ações é importante por conta que umas precisam de alvo e outras não.
        self.acoes_ataque: dict[int, Callable[[], int]] = {
            PALADINO.ATAQUE_BASICO.ID: self.atacar,
            PALADINO.ATAQUE_ESPECIAL.ID: self.ataque_especial
        }

        self.acoes_buff: dict[int, Callable[[], None]] = {
            PALADINO.RECUPERAR_FOLEGO.ID: self.recuperar_folego
        }

        

    #Acoes
    def atacar(self) -> list[Command]:
        """Ataque básico do paladino em combate."""
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        alvo = self.escolher_alvo()
        
        if alvo == None:
            raise ValueError("Alvo nulo.")

        if rolagem == Combate.CRITICO:
            self.mana += PALADINO.STATUS_MAGO.RESTAURACAO_MANA_CRITICO
        
        comandos: list[Command] = [CommandAtaqueBasico(PALADINO.ATAQUE_BASICO, alvo, rolagem)]

        return comandos

    def recuperar_folego(self) -> None:
        """Ação de cura do paladino em combate."""
        cura = self.rolar_dados(PALADINO.TIPO_DADO_RECUPERAR_FOLEGO,PALADINO.QUANTIDADE_DADOS_RECUPERAR_FOLEGO)
        print(f'\nVocê respira fundo e consegue recuperar parte da sua força.\n[[Curou {cura} de vida]]\n[[Recuperou 1 de stamina]]')

        self.vida = min(self.vida + cura, PALADINO.VIDA)
        self.mana += PALADINO.RESTAURACAO_MANA_RECUPERAR_FOLEGO


    def ataque_especial(self) -> int:
        """Ataque especial do paladino em combate."""
        if self.mana < PALADINO.CUSTO_ATAQUE_ESPECIAL:
            print("Mana insuficiente! Turno perdido...")
            return 0
        
        print('\nVocê levanta sua espada, exibindo uma luz divina e vai pra cima do alvo com tudo o que tem, e...')
        
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        self.mana -= PALADINO.CUSTO_ATAQUE_ESPECIAL
        atkJ = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        
        if atkJ == Combate.FALHA:
            print('\nInfelizmente você erra o ataque.')
            return 0
        
        elif atkJ == Combate.CRITICO:
            print(f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 50 de dano]]{Cores.RESET}')
            return PALADINO.DANO_ATAQUE_ESPECIAL * PALADINO.MULTIPLICADOR_CRITICO
        
        else:
            print('\nVocê acerta seu golpe no alvo!\n[[Causou 25 de dano]]')
            return PALADINO.DANO_ATAQUE_ESPECIAL


    #Menus
    """def menu_ataque(self) -> None:
        Cria um menu para a escolha de ações de ataque.
        print(f"{PALADINO.ATAQUE_BASICO.ID}- Atacar (dano em 1 alvo)")
        if self.mana >= PALADINO.ATAQUE_ESPECIAL.CUSTO:
            print(f'{PALADINO.ATAQUE_ESPECIAL.ID} - ATAQUE ESPECIAL disponível! (25 de dano normal/50 de dano crítico)')
        comandos = self.gerenciar_menu_ataque()
        return comandos

    
    def menu_buffs(self) -> None:
        Cria um menu para a escolha de ações de buff.
        print(f"{PALADINO.RECUPERAR_FOLEGO.ID} - Se recuperar (Se cura em 2d8 e + 1 de stamina)")
        self.gerenciar_menu_buffs()
    """

    #Outros metodos
    def turno(self) -> list[Command]:
        """Gerencia o turno do paladino em combate."""
        comandos = self.menu_acoes()
        return comandos
