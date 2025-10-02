# Classe Paladino
#Libs
from game_data import Combate
from ...configuracoes.criaturas.configurações_jogadores import PALADINO
from ..base import CriaturaBase
from interfaces import ICriatura, ICommand, AtributosMagicos
from typing import Callable
from ...commands.ataques import CommandAtaqueBasico



class Paladino(CriaturaBase[AtributosMagicos]):
    """Classe especifica para criar um paladino."""
    def __init__(self, configuracoes: PALADINO = PALADINO()):
        """Cria uma instância de paladino com suas características básicas."""
        super().__init__(configuracoes.nome, configuracoes.atributos)

        self.configuracoes = configuracoes

        self.acoes: dict[int, Callable[[list[ICriatura] | None], list[ICommand]]] = {
            int(configuracoes.ataques['ataque_basico']['id']): lambda alvo: self.atacar(alvo),
            int(configuracoes.ataques['ataque_especial']['id']): lambda alvo: self.ataque_especial(alvo),
            int(configuracoes.ataques['recuperar_folego']['id']): lambda not_alvo = None: self.recuperar_folego(not_alvo)
        }

        self.acoes[1].__name__ = 'ataque_basico'
        self.acoes[2].__name__ = 'ataque_especial'
        self.acoes[3].__name__ = 'recuperar_folego'
        

    #Acoes
    def atacar(self, alvo: list[ICriatura] | None) -> list[ICommand]:
        """Ataque básico do paladino em combate."""
        if alvo == None:
            raise ValueError("Alvo inválido no momento do ataque!")
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        comandos: list[ICommand] = [CommandAtaqueBasico(rolagem, self.configuracoes.ataques['ataque_basico'], alvo)]


        if rolagem == Combate.CRITICO:
            self.atributos['mana_atual'] += min(self.atributos['mana_maxima'], self.atributos['mana_maxima'] + self.configuracoes.atributos['restauracao_mana_critico'])


        return comandos


    def recuperar_folego(self, alvo: list[ICriatura] | None = None) -> list[ICommand]:
        """Ação de cura do paladino em combate."""
        cura = self.rolar_dados(PALADINO.TIPO_DADO_RECUPERAR_FOLEGO,PALADINO.QUANTIDADE_DADOS_RECUPERAR_FOLEGO)
        print(f'\nVocê respira fundo e consegue recuperar parte da sua força.\n[[Curou {cura} de vida]]\n[[Recuperou 1 de stamina]]')

        self.vida = min(self.vida + cura, PALADINO.VIDA)
        self.mana += PALADINO.RESTAURACAO_MANA_RECUPERAR_FOLEGO


    def ataque_especial(self, alvo: list[ICriatura] | None) -> list[ICommand]:
        """Ataque especial do paladino em combate."""
        if alvo == None:
            raise ValueError("Alvo inexistente.")
        
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
