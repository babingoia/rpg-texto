# Libs
from models.Criatura import Criatura
from models.Jogador import Jogador
from models.Lich import Lich
from models.batalha import Batalha


#Variaveis globais
criaturas: list[Criatura] = []


#Main
while True:
    ready = input('Bem vindo ao Lich Boss Battle!\nDigite 1 para começar.\n')

    if ready == '1':
        print('\nVocê percorreu um longo caminho até aqui, enfrentou diversos inimigos, salvou inúmeros seres indefesos.\nE agora finalmente está de frente para ele, o General dos Mortos, Lich.')
        print()
        break
    else:
        print('\nQue pena, talvez você precise de um pouco mais de tempo para se preparar então.\n')
        exit()

lich = Lich()
jogador = Jogador()

criaturas.append(lich)
criaturas.append(jogador)

batalha = Batalha(criaturas)

vencedor = batalha.iniciar()

if vencedor == jogador:
    print('\nApesar de todo o seu esforço, não foi o suficiente.\nVocê morreu, e o grande General dos Mortos sai vitorioso por mais uma era.')
elif vencedor == lich: # type: ignore
    print('\nINCRÍVEL!!! Você conseguiu derrotar o temido Lich.\nDepois de todos os perrengues, o seu esforço deu resultados. Meus parabéns!\nVocê zerou o jogo.')