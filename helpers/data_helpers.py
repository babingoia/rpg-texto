#Funções genéricas para manipulação de dados
#libs
from typing import Any
from interfaces import ICriatura

#Defs
def convert_to_str(dados: dict[Any, Any], assinatura_erro: str) -> dict[str, str]:
    dados_convertidos: dict[str, str] = {}
    try:
        for chave, valor in dados.items():
            dados_convertidos[str(chave)] = str(valor)
        
        return dados_convertidos
    except Exception as erro:
        raise ValueError(f'Erro ao converter dicionário para str, str {assinatura_erro}, {erro}')


def validar_chaves_dicionario(dados: dict[Any, Any], chaves: list[Any], assinatura_erro: str):

    for chave in chaves:
        if not dados.get(chave):
            raise ValueError(f"Ops, dados incorretos para criação de uma instância de {assinatura_erro}.")


def validar_lista_criatura(dados: list[Any], assinatura_erro: str) -> list[ICriatura]:
    
    lista_validada: list[ICriatura] = []

    for element in dados:
        if not isinstance(element, ICriatura):
            raise ValueError(f"Ops, dados incorretos para a validação da instância de {assinatura_erro}")
        
        lista_validada.append(element)

    return lista_validada


def validar_dict_lista_criaturas(dados: dict[Any, Any], assinatura_erro: str) -> dict[str, list[ICriatura]]:
    
    dict_validado: dict[str, list[ICriatura]] = {}
    
    for chave, item in dados.items():
        if not isinstance(chave, str):
            raise ValueError(f'Chave do dicionario não é uma strig. {assinatura_erro}')
        
        dict_validado[chave] = validar_lista_criatura(item, assinatura_erro)
    
    return dict_validado
