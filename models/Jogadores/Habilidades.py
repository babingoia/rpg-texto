#Commands para habilidades
#libs
import configs as cfg
from Criatura import Criatura
import random
import time

#Classe Abstrata
class Command:
    """Classe abstrata para criar ataques."""
    def __init__(self, configuracoes: cfg.CriaturaCFG, executor: Criatura, alvos: list[Criatura]) -> None:
        self.executor = executor
        self.alvos = alvos
        self.configuracoes = configuracoes

    
    def executar (self) -> int:
        raise NotImplementedError


#Subclasses
class CommandAtaqueBasico(Command):
    """Subclasse que executa um ataque básico."""
    def __init__(self, configuracoes: cfg.CriaturaCFG, executor: Criatura, alvos: list[Criatura]) -> None:
        super().__init__(configuracoes, executor, alvos)
    

    def checar_efeito(self, rolagem: int):
        match self.configuracoes.ATAQUE_BASICO_EFEITO:
            case 'cura':
                self.aplicar_cura(rolagem)
            case _:
                pass


    def aplicar_cura(self, rolagem: int):
        if rolagem == cfg.Combate.CRITICO:
            self.executor.vida += self.configuracoes.CURA * self.configuracoes.MULTIPLICADOR_CRITICO
        elif rolagem == cfg.Combate.FALHA:
            self.executor.vida += 


    def executar(self) -> int:
        print(self.configuracoes.MENSAGEM_INICIO)
        self.contagem_regressiva(cfg.Combate.DELAY_MEDIO)
        rolagem = self.rolar_dados(cfg.Combate.ROLAGEM_PADRAO, 1)
        ataque: int = 0
        
        if rolagem == cfg.Combate.FALHA:
            print(self.configuracoes.MENSAGEM_FALHA)
            ataque = cfg.Combate.DANO_FALHA
        
        elif rolagem == cfg.Combate.CRITICO:
            print(self.configuracoes.MENSAGEM_CRITICO)

            ataque = self.configuracoes.DANO_ATAQUE_BASICO * self.configuracoes.MULTIPLICADOR_CRITICO
        
        else:
            print(self.configuracoes.MENSAGEM_NORMAL)
            ataque = self.configuracoes.DANO_ATAQUE_BASICO

        self.checar_efeito(rolagem)
        return ataque