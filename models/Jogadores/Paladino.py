# Classe Paladino
#Libs
from configs import PALADINO, Combate, Dados, Cores
from .jogador import Jogador
from typing import Union, Callable


class Paladino(Jogador):
    """Classe especifica para criar um paladino."""
    def __init__(self):
        """Cria uma instância de paladino com suas características básicas."""
        super().__init__()
        self.nome = PALADINO.NOME
        self.vida: int = PALADINO.VIDA
        self.mana: int = PALADINO.MANA

        #Esse distinção de ações é importante por conta que umas precisam de alvo e outras não.
        self.acoes_ataque: dict[int, Callable[[], int]] = {
            PALADINO.ID_ATAQUE_BASICO: self.atacar,
            PALADINO.ID_BOLA_FOGO: self.bola_de_fogo,
            PALADINO.ID_ATAQUE_ESPECIAL: self.ataque_especial
        }

        self.acoes_buff: dict[int, Callable[[], None]] = {
            PALADINO.ID_RECUPERAR_FOLEGO: self.recuperar_folego
        }

        

    #Acoes
    def atacar(self) -> int:
        """Ataque básico do paladino em combate."""
        print('\nVocê segura sua espada com força, e vai pra cima do alvo, e...')
        
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        rolagem = self.rolar_dados(Dados.D6, 1)
        
        if rolagem == Combate.FALHA:
            print('\nInfelizmente você erra o ataque.')
            return Combate.DANO_FALHA
        
        elif rolagem == Combate.CRITICO:
            print(f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 20 de dano]]\n[[Recuperou 1 de stamina]]{Cores.RESET}')
            self.mana += PALADINO.RESTAURACAO_MANA_CRITICO
            return PALADINO.DANO_ATAQUE_BASICO * PALADINO.MULTIPLICADOR_CRITICO
        
        else:
            print('\nVocê acerta seu golpe no alvo!\n[[Causou 10 de dano]]')
            return 10


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
        atkJ = self.rolar_dados(Dados.D6, 1)
        
        if atkJ == Combate.FALHA:
            print('\nInfelizmente você erra o ataque.')
            return 0
        
        elif atkJ == Combate.CRITICO:
            print(f'{Cores.YELLOW}\nVocê acerta um golpe crítico!!!\n[[Causou 50 de dano]]{Cores.RESET}')
            return PALADINO.DANO_ATAQUE_ESPECIAL * PALADINO.MULTIPLICADOR_CRITICO
        
        else:
            print('\nVocê acerta seu golpe no alvo!\n[[Causou 25 de dano]]')
            return PALADINO.DANO_ATAQUE_ESPECIAL


    def bola_de_fogo(self) -> int:
        """Ataque em área do paladino em combate."""
        N_PRA_NAO_DAR_ERRO = 0
        if self.batalha == None:
            return N_PRA_NAO_DAR_ERRO
        
        print('\nVocê junta a suas mãos e começa a canalizar, uma energia magica começa a surgir e...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        rolagem = self.rolar_dados(Dados.D6, 1)
        
        if rolagem == Combate.FALHA:
            print('\nA magia se desfaz no ar.')
            return N_PRA_NAO_DAR_ERRO
        
        elif rolagem == Combate.CRITICO:

            dano = PALADINO.DANO_BOLA_FOGO * PALADINO.MULTIPLICADOR_CRITICO

            print(f'{Cores.YELLOW}\nVocê acerta ela numa explosão enorme!!!\n[[Causou {dano} de dano em todos os alvos]]\n[[Recuperou {PALADINO.RESTAURACAO_MANA_CRITICO} de mana]]{Cores.RESET}')
            
            self.mana += PALADINO.RESTAURACAO_MANA_CRITICO
            
            for inimigo in self.batalha.inimigos:
                inimigo.vida -= dano
            return N_PRA_NAO_DAR_ERRO
        
        else:
            dano = PALADINO.DANO_BOLA_FOGO

            print(f'\nVocê acerta seu golpe e todos os inimigos sofrem queimaduras!\n[[Causou {dano} de dano em todos os alvos]]')

            for inimigo in self.batalha.inimigos:
                inimigo.vida -= dano
            return N_PRA_NAO_DAR_ERRO


    #Menus
    def menu_ataque(self) -> None:
        """Cria um menu para a escolha de ações de ataque."""
        print(f"{PALADINO.ID_ATAQUE_BASICO}- Atacar (dano em 1 alvo)")
        print(f"{PALADINO.ID_BOLA_FOGO} - Bola de fogo (dano em área)")
        if self.mana >= PALADINO.CUSTO_ATAQUE_ESPECIAL:
            print(f'{PALADINO.ID_ATAQUE_ESPECIAL} - ATAQUE ESPECIAL disponível! (25 de dano normal/50 de dano crítico)')
        self.gerenciar_menu_ataque()

    
    def menu_buffs(self) -> None:
        """Cria um menu para a escolha de ações de buff."""
        print(f"{PALADINO.ID_RECUPERAR_FOLEGO} - Se recuperar (Se cura em 2d8 e + 1 de stamina)")
        self.gerenciar_menu_buffs()


    #Outros metodos
    def mostrar_stats(self) -> None:
        """Mostra os status do paladino"""
        print('\nVida do Paladino: {}'.format(self.vida))
        print('Mana do Paladino: {}'.format(self.mana))
        print()

    
    def turno(self) -> Union[int, None]:
        """Gerencia o turno do paladino em combate."""
        self.menu_acoes()
