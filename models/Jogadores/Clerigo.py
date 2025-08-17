#Classe do clérigo
#libs
from .jogador import Jogador
from models.Gerenciadores.batalha import Batalha
from ..Configs.configs import CLERIGO, Combate, Cores


#Classes
class Clerigo(Jogador):
    def __init__(self, batalha: Batalha | None = None) -> None:
        super().__init__(batalha)
        self.nome = CLERIGO.NOME
        self.vida: int = CLERIGO.VIDA
        self.mana: int = CLERIGO.MANA_INICIAL

        self.acoes_ataque = {
            CLERIGO.ID_BOLA_FOGO: self.bola_de_fogo
        }

        self.acoes_buff = {
            CLERIGO.ID_MEDITACAO: self.meditacao
        }
    

    #Acoes Ataque
    def bola_de_fogo(self) -> int:
        """Ataque em área do paladino em combate."""
        N_PRA_NAO_DAR_ERRO = 0
        if self.batalha == None:
            return N_PRA_NAO_DAR_ERRO
        
        if self.mana < CLERIGO.CUSTO_BOLA_FOGO:
            print("Mana insuficiente, uma pequena aura magica se forma e some instantaneamente.")
            return 0
        
        print('\nVocê junta a suas mãos e começa a canalizar, uma energia magica começa a surgir e...')
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        self.mana -= CLERIGO.CUSTO_BOLA_FOGO
        
        if rolagem == Combate.FALHA:
            print('\nA magia se desfaz no ar.')
            return N_PRA_NAO_DAR_ERRO
        
        elif rolagem == Combate.CRITICO:

            dano = CLERIGO.DANO_BOLA_FOGO * CLERIGO.MULTIPLICADOR_CRITICO

            print(f'{Cores.YELLOW}\nVocê acerta ela numa explosão enorme!!!\n[[Causou {dano} de dano em todos os alvos]]\n[[Recuperou {CLERIGO.RESTAURACAO_MANA_CRITICO} de mana]]{Cores.RESET}')
            
            self.mana += CLERIGO.RESTAURACAO_MANA_CRITICO
            
            for inimigo in self.batalha.inimigos:
                inimigo.vida -= dano
            return N_PRA_NAO_DAR_ERRO
        
        else:
            dano = CLERIGO.DANO_BOLA_FOGO

            print(f'\nVocê acerta seu golpe e todos os inimigos sofrem queimaduras!\n[[Causou {dano} de dano em todos os alvos]]')

            for inimigo in self.batalha.inimigos:
                inimigo.vida -= dano
            return N_PRA_NAO_DAR_ERRO
        

    #Acoes de Buff
    def meditacao(self):
        print(f"{self.nome} se senta e começa a meditar, sua mente se acalma e uma suave aura dourada surge...")
        self.contagem_regressiva(Combate.DELAY_MEDIO)
        atkj = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        restauracao = CLERIGO.RECUPERACAO_MANA_MEDITACAO

        if atkj == Combate.CRITICO:
            restauracao *= CLERIGO.MULTIPLICADOR_CRITICO
            
            print(f'{Cores.YELLOW}\n Sua aura se intensifica e seu corpo começa a flutuar!!!\n [[Recuperou {restauracao} de mana]]{Cores.RESET}')

            self.mana = min(self.mana + restauracao, CLERIGO.MANA_MAXIMA)
        
        elif atkj == Combate.FALHA:
            print(f"{Cores.RED}\n {self.nome} não consegue se acalmar e a aura desaparece.{Cores.RESET}")
        
        else:
            print(f"{self.nome} após sua concentração se sente mais revigorado. [[Recuperou {restauracao} de mana]]")
            self.mana = min(self.mana + restauracao, CLERIGO.MANA_MAXIMA)
    

    #MENUS
    def menu_ataque(self) -> None:
        print(f"{CLERIGO.ID_BOLA_FOGO} - Bola de Fogo (Causa {CLERIGO.DANO_BOLA_FOGO} de dano + {CLERIGO.EFEITO_BOLA_FOGO}. Custa {CLERIGO.CUSTO_BOLA_FOGO} de mana)")
        self.gerenciar_menu_ataque()
    

    def menu_buffs(self) -> None:
        print(f"{CLERIGO.ID_MEDITACAO} - Meditação (Recupera {CLERIGO.RECUPERACAO_MANA_MEDITACAO} mana)")
        self.gerenciar_menu_buffs()


    #Outros
    def turno(self) -> int | None:
        self.menu_acoes()
