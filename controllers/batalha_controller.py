#Classe concreta para instâncias de batalha.
#Libs
from interfaces import ICriatura, ICommand, IBatalha, BatalhaData, BatalhaInicioTurno, BatalhaFinalTurno, BatalhaFinal, Escolhas, IViewSubscriber
from .batalha_subject import BaseBatalhaSubject
from random import shuffle
from typing import Union


#Classes
class Batalha(IBatalha, BaseBatalhaSubject, IViewSubscriber):
    """Classe que gerencia as batalhas.
        -> Necessita uma configuração inicial de criaturas.
    """
    def __init__(self, criaturas: BatalhaData) -> None:
        """Faz a criação de uma instância de batalha.
            
        Args:
            inimigos: Lista de inimigos dentro da batalha.
            jogadores: Lista de jogadores dentro da batalha.
        """
        super().__init__()
        self.jogador_escolhas: Escolhas
        self.dados = criaturas


    def get_input_update(self, escolhas: Escolhas) -> None:
        self.jogador_escolhas = escolhas


    def checar_morte(self, dados: BatalhaData):
        """Verifica se algum inimigo morreu e remove ele do combate."""
        inimigos_vivos: list[ICriatura] = []
        jogadores_vivos: list[ICriatura] = []

        for inimigo in dados['inimigos']:
            atributos = inimigo.get_atributos()
            if atributos['vida_atual'] > 0:
                inimigos_vivos.append(inimigo)
            else:
                print(f"{inimigo.get_nome()} foi destruido!")

        for jogador in dados['jogadores']:
            atributos = jogador.get_atributos()
            if atributos['vida_atual'] > 0:
                jogadores_vivos.append(jogador)
            else:
                print(f"{jogador.get_nome()} foi destruido!")

        criaturas_vivas: dict[str, list[ICriatura]] = {}
        criaturas_vivas['inimigos'] = list(inimigos_vivos)
        criaturas_vivas['jogadores'] = list(jogadores_vivos)

        self.dados['inimigos'] = criaturas_vivas['inimigos']
        self.dados['jogadores'] = criaturas_vivas['jogadores']


    def randomizar_turno(self) -> None:
        
        criaturas: list[ICriatura] = self.dados['inimigos'] + self.dados['jogadores']
        
        shuffle(criaturas)

        self.dados['ordem_turnos'] = list(criaturas)


    def iniciar(self) -> None:
        """Inicia o loop de Batalha
        
        Returns:
            Criatura: Retorna quem venceu a batalha.
        """

        self.battle_start_notify(self.dados)

        #Começa o loop de batalha
        while len(self.dados['jogadores']) > 0 and len(self.dados['inimigos']) > 0:
            self.randomizar_turno()
            for criatura in self.dados['ordem_turnos']:
                
                acoes = criatura.get_acoes()

                turn_start_data: BatalhaInicioTurno = {
                    'criaturas': self.dados,
                    'criatura_atual': criatura,
                    'acoes_disponiveis': acoes
                }

                self.turn_start_notify(turn_start_data)
                 
                comandos: list[ICommand] = criatura.executar_acao(
                    self.jogador_escolhas['acao_escolhida'].getValue(),
                    self.jogador_escolhas['alvo_selecionado']
                    )
                
                acoes_executadas: list[dict[str, Union[str, int]]] = []
                
                for comando in comandos:
                    acao_executada = comando.executar()
                    acoes_executadas.append(acao_executada)
                
                self.checar_morte(self.dados)

                turn_end_data: BatalhaFinalTurno = {
                    'acoes_executadas': acoes_executadas,
                    'criatura_atual': criatura,
                    'criaturas': self.dados
                }

                self.turn_end_notify(turn_end_data)
            
        
        if len(self.dados['inimigos']) > 0:
            end_battle_data: BatalhaFinal = {
            'criaturas': self.dados['inimigos']
            }
        else:
            end_battle_data: BatalhaFinal = {
                'criaturas': self.dados['jogadores']
            }

        self.battle_end_notify(end_battle_data)
