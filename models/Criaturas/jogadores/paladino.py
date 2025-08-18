# Classe Paladino
#Libs
from configuracoes import PALADINO, Combate
from ..base import Jogador
from typing import Callable
from commands import Command, CommandAtaqueBasico, CommandRecuperarVida, CommandRecuperarMana

cfg = PALADINO()

class Paladino(Jogador):
    """Classe especifica para criar um paladino."""
    def __init__(self):
        """Cria uma instância de paladino com suas características básicas."""
        super().__init__()
        self.nome = cfg.STATUS.NOME
        self.vida_maxima: int = cfg.STATUS.VIDA
        self.vida: int = self.vida_maxima
        self.mana_maxima: int = cfg.STATUS_MAGO.MANA_MAXIMA
        self.mana = 0

        self.acoes: dict[int, Callable[[], list[Command]]] = {
            cfg.ATAQUE_BASICO.ID: self.atacar,
            cfg.ATAQUE_ESPECIAL.ID: self.ataque_especial,
            cfg.RECUPERAR_FOLEGO.ID: self.recuperar_folego
        }

        self.acoes_especiais: dict[int, Callable[[], list[Command]]] = {
            cfg.ATAQUE_ESPECIAL.ID: self.ataque_especial
        }


    #Acoes
    def atacar(self) -> list[Command]:
        """Ataque básico do paladino em combate."""
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        alvo = self.escolher_alvo()

        if rolagem == Combate.CRITICO:
            self.mana += cfg.STATUS_MAGO.RESTAURACAO_MANA_CRITICO
        
        comandos: list[Command] = [CommandAtaqueBasico(cfg.ATAQUE_BASICO, alvo, rolagem)]

        return comandos
    

    def ataque_especial(self) -> list[Command]:
        """Ataque especial do paladino em combate."""
        if self.mana < cfg.ATAQUE_ESPECIAL.CUSTO:
            print("Você se concentra para canalizar todo o poder que consegue em sua espada... mas não é o suficiente. [[Mana Insuficiente!]]")
            return []
        
        rolagem = self.rolar_dados(Combate.ROLAGEM_PADRAO, 1)
        alvo = self.escolher_alvo()

        ataque: Command = CommandAtaqueBasico(cfg.ATAQUE_ESPECIAL, alvo, rolagem)
        comandos: list[Command] = [ataque]

        self.mana -= cfg.ATAQUE_ESPECIAL.CUSTO
        
        return comandos

        
    def recuperar_folego(self) -> list[Command]:
        """Ação de cura do paladino em combate."""

        rolagem_vida = self.rolar_dados(cfg.RECUPERAR_FOLEGO.VIDA.TIPO_DADO, cfg.RECUPERAR_FOLEGO.VIDA.QUANTIDADE_DADOS)
        rolagem_mana = cfg.RECUPERAR_FOLEGO.MANA.QUANTIDADE
        print(rolagem_mana)
        
        print(cfg.RECUPERAR_FOLEGO.MENSAGENS.MENSAGEM_INICIO, f'[[recuperou {rolagem_vida} pontos de vida e {rolagem_mana} de mana]]')

        comando_rec_vida: Command = CommandRecuperarVida(rolagem_vida, self)
        comando_rec_mana: Command = CommandRecuperarMana(rolagem_mana, self)

        comandos: list[Command] = [comando_rec_vida, comando_rec_mana]

        return comandos


    #Outros metodos
    def turno(self) -> list[Command]:
        """Gerencia o turno do paladino em combate."""
        comandos = self.menu_acoes(self.acoes)
        return comandos
