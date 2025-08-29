#Classe concreta para instâncias de batalha.
#Libs
from interfaces import ICriatura, ICommand, IDataFactory, IViewFactory, IData, IAtaqueStrategyFactory, IBatalha
from typing import Callable, cast
from inspect import signature
from helpers import convert_to_message

#Classes
class Batalha(IBatalha):
    """Classe que gerencia as batalhas.
        -> Necessita uma configuração inicial de criaturas.
    """
    def __init__(self, view_factory: IViewFactory, data_factory: IDataFactory, jogadores: list[ICriatura], inimigos: list[ICriatura], strategy_factory: IAtaqueStrategyFactory) -> None:
        """Faz a criação de uma instância de batalha.
            
        Args:
            inimigos: Lista de inimigos dentro da batalha.
            jogadores: Lista de jogadores dentro da batalha.
        """
        self.view_factory = view_factory
        self.data_factory = data_factory
        self.strategy_factory = strategy_factory

        self.tela = view_factory.criar('batalha')
        self.dados = data_factory.criar('batalha', {'inimigos': inimigos, 'jogadores': jogadores})


    def get_inimigos(self) -> list[ICriatura]:
        return super().get_inimigos()
    

    def get_jogadores(self) -> list[ICriatura]:
        return super().get_jogadores()


    def checar_morte(self, dados: dict[str, list[ICriatura]]):
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

        self.dados.update(criaturas_vivas)


    def get_atributos_mensagens(self, dados: dict[str, list[ICriatura]]) -> list[IData]:
        
        mensagens: list[IData] = []

        mensagens.append(self.data_factory.criar('view', {'titulo': 'inimigos'}))

        for inimigo in dados['inimigos']:
            atributos  = inimigo.get_atributos()
            mensagens.append(self.data_factory.criar('view', atributos))

        mensagens.append(self.data_factory.criar('view', {'titulo': 'jogadores'}))

        for jogador in dados['jogadores']:
            atributos = jogador.get_atributos()
            mensagens.append(self.data_factory.criar('view', atributos))

        return mensagens


    def acoes_to_mensagens(self, acoes: dict[int, Callable[[ICriatura], list[ICommand]]]) -> IData:
        mensagem_dict: dict[str, str] = {}
        
        for chave, valor in acoes.items():
            mensagem_dict[str(chave)] = valor.__name__
        
        mensagem: IData = self.data_factory.criar('view', mensagem_dict)

        return mensagem


    def mostrar_mensagens(self, mensagens: list[IData]):
        for mensagem in mensagens:
            self.tela.mostrar(mensagem)


    def get_alvo(self, dados: dict[str, list[ICriatura]]) -> ICriatura:           
            mensagens: list[IData] = convert_to_message([{
                '': 'Deseja acertar um jogador ou um inimigo?'
            }, {'1': 'jogador'}, {'2': 'inimigo'}], self.data_factory, 'BatalhaController')

            self.mostrar_mensagens(mensagens)
            tipo_alvo = self.tela.get_input([1,2])

            if tipo_alvo == 1:
                tipo_alvo = 'jogadores'
            else:
                tipo_alvo = 'inimigos'
            
            mensagens = convert_to_message(
                {chave: criatura.get_nome() for chave, criatura in enumerate(dados[tipo_alvo])}, self.data_factory,
                ' batalhaController.')
            
            self.mostrar_mensagens(mensagens)
            escolha = self.tela.get_input()

            alvo = dados[tipo_alvo][escolha]
            
            return alvo


    def iniciar(self) -> str:
        """Inicia o loop de Batalha
        
        Returns:
            Criatura: Retorna quem venceu a batalha.
        """
        dados = self.dados.get_data()

        dados = cast(dict[str, list[ICriatura]], dados)


        #Começa o loop de batalha
        while len(dados['jogadores']) > 0 and len(dados['inimigos']) > 0:
            for lista_criaturas in dados.values():
                for criatura in lista_criaturas:
                    
                    mensagens = self.get_atributos_mensagens(dados)
                    self.mostrar_mensagens(mensagens)
                    

                    acoes = criatura.get_acoes()
                    self.tela.mostrar(self.acoes_to_mensagens(acoes))
                    
                    
                    escolha = self.tela.get_input(list(acoes.keys()))
                    alvo = None

                    if 'alvo' in signature(acoes[escolha]).parameters:
                        if criatura in dados['jogadores']:
                            alvo = self.get_alvo(dados)
                        else:
                            estrategia = self.strategy_factory.criar('random_agressive', conjurador=criatura)
                            alvo = estrategia.escolher_alvo(dados)

                    comandos: list[ICommand] = criatura.executar_acao(escolha, alvo)
                    
                    for comando in comandos:
                        mensagem = comando.executar()
                        self.mostrar_mensagens(mensagem)
                    
                    self.checar_morte(dados)

                    input("Aperte ENTER para continuar...")
                    self.tela.limpar_tela()
            
        if len(dados['inimigos']) > 0:
            return 'inimigos'
        else:
            return 'jogadores'

