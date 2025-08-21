# Classe Paladino
#Libs
from configuracoes import PALADINO, Combate
from ..base import CriaturaBase
from interfaces import ICriatura, ICommand
from typing import Callable
from commands import CommandAtaqueBasico



class Paladino(CriaturaBase):
    """Classe especifica para criar um paladino."""
    def __init__(self, configuracoes: PALADINO = cfg):
        """Cria uma instância de paladino com suas características básicas."""
        super().__init__(configuracoes.NOME, configuracoes.ATRIBUTOS)

        self.configuracoes = configuracoes

        self.acoes: dict[int, Callable[[ICriatura], list[ICommand]]] = {
            configuracoes.ATAQUE_BASICO['id']: lambda alvo: self.atacar(alvo),
            configuracoes.ATAQUE_ESPECIAL['id']: lambda alvo: self.ataque_especial(alvo),
            configuracoes.RECUPERAR_FOLEGO['id']: lambda: self.recuperar_folego()
        }
        

    #Acoes
    def atacar(self, alvo: ICriatura) -> list[ICommand]:
        """Ataque básico do paladino em combate."""
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        comandos: list[ICommand] = [CommandAtaqueBasico(self.nome, rolagem, self.configuracoes.ATAQUE_BASICO, alvo)]


        if rolagem == Combate.CRITICO:
            self.atributos['mana_atual'] += min(self.atributos['mana_maxima'], self.atributos['mana_maxima'] + self.configuracoes.ATRIBUTOS['restauracao_mana_critico'])


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
