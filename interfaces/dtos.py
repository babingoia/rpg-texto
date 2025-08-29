#Implementações concretas de estruturas de dados.
#Libs
from dataclasses import dataclass
from typing import Any
from interfaces import ICriatura, IData, IDataFactory
from helpers import validar_lista_criatura, validar_chaves_dicionario, convert_to_str

#SubClasses
@dataclass
class BatalhaData(IData):
    def __init__(self, inimigos: list[ICriatura], jogadores: list[ICriatura]) -> None:
        
        self.criaturas: dict[str, list[ICriatura]] = {
            'inimigos': inimigos,
            'jogadores': jogadores
        }

        self.inimigos = self.criaturas['inimigos']
        self.jogadores = self.criaturas['jogadores']
    

    def get_data(self) -> dict[str, Any]:
        data: dict[str, Any] = self.criaturas.copy()
        data['criaturas'] = self.inimigos + self.jogadores
        return data


    def add(self, chave: str, valor: ICriatura) -> None:
        match chave:
            case 'inimigos':
                self.inimigos.append(valor)
            case 'jogadores':
                self.jogadores.append(valor)
            case _:
                raise ValueError('Criatura não identificada.')
    

    def remove(self, chave: str, valor: ICriatura) -> None:
        match chave:
            case 'inimigo':
                self.inimigos.remove(valor)
            case 'jogador':
                self.jogadores.remove(valor)
            case _:
                raise ValueError('Criatura não identificada.')
    

    def update(self, dados: dict[Any, Any]) -> None:
        validar_chaves_dicionario(dados, ['inimigos', 'jogadores'], 'batalhaData')

        jogadores: list[ICriatura] = validar_lista_criatura(dados['jogadores'], 'batalhaData')
        inimigos: list[ICriatura] = validar_lista_criatura(dados['inimigos'], 'BatalhaData')

        self.__init__(inimigos, jogadores)


@dataclass
class ViewData(IData):
    def __init__(self, dados: dict[str, str]) -> None:
        
        self.dados: dict[str, str] = {}

        for chave, valor in dados.items():
            dados[str(chave)] = str(valor)
        

    def get_data(self) -> dict[str, str]:
        data = self.dados.copy()
        return data
    

    def add(self, chave: Any, valor: Any) -> None:
        return super().add(chave, valor)
    
    
    def remove(self, chave: Any, valor: Any) -> None:
        return super().remove(chave, valor)

    
    def update(self, dados: dict[str, str]) -> None:
        self.__init__(dados)


        
class DataFactory(IDataFactory):

    @staticmethod
    def criar(tipo: str, dados: dict[Any, Any]={}) -> IData:
        match tipo:
            case 'view':
                dados = convert_to_str(dados, 'DataFactory: view obj')
                return ViewData(dados)
            
            case 'batalha':
                validar_chaves_dicionario(dados, ['inimigos', 'jogadores'], 'batalhaData')

                jogadores: list[ICriatura] = validar_lista_criatura(dados['jogadores'], 'batalhaData')
                inimigos: list[ICriatura] = validar_lista_criatura(dados['inimigos'], 'BatalhaData')

                return BatalhaData(jogadores, inimigos)
            case _:
                raise ValueError('Objeto para criação não encontrado!')


"""@dataclass
class AtributosData(Data):
    def __init_subclass__(cls, atributos: dict[str, int], nome: str = 'atributos') -> None:
        cls.nome = nome
        cls.atributos = atributos
    

    def get_data(self) -> dict[str, Any]:
        data: dict[str, Any] = self.atributos.copy()
        data['nome'] = self.nome
        return data
    

    def get_for_view(self) -> dict[str, str]:
        data: dict[str, str] = {}

        for chave, valor in self.dict

    
    def add(self, chave: str, valor: Any) -> None:
        self.atributos[chave] = valor
    

    def remove(self, chave: str, valor: Any) -> None:
        if self.atributos[chave]:
            del self.atributos[chave]
            return
    

@dataclass
class AcoesData(Data):
    def __init_subclass__(cls, acoes: dict[int, Callable[[ICriatura], list[ICommand]]], nome: str = 'acoes') -> None:
        cls.nome = nome
        cls.acoes = acoes


    def get_for_view(self) -> dict[str, str]:
        data: dict[str, str] = {}

        for chave, valor in self.acoes.items():
            data[str(chave)] = valor.__name__
        
        data['nome'] = self.nome

        return data


    def get_data(self) -> dict[int, Callable[[ICriatura], list[ICommand]]]:
        data = self.acoes.copy()
        return data
    

    def add(self, chave: int, valor: Callable[[Any], list[ICommand]]) -> None:
        self.acoes[chave] = valor
    

    def remove(self, chave: int, valor: Callable[[Any], list[ICommand]]) -> None:
        if self.acoes.get(chave):
            del self.acoes[chave]
            return

        if valor in self.acoes.values():
            chaves_del = [chave for chave, valor_dict in self.acoes.items() if valor_dict == valor]
            for chave_del in chaves_del:
                del self.acoes[chave_del]
            return

        raise ValueError('Chave e valor nao encontrados!')"""
        