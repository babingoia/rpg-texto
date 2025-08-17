#Inicia o programa
# Libs
from models.Criatura import Criatura
from models.Jogadores.Paladino import Paladino
from models.Jogadores.Assassino import Assassino
from models.Jogadores.Clerigo import Clerigo
from models.Inimigos.Lich import Lich
from models.Gerenciadores.batalha import Batalha
from models.Jogadores.jogador import Jogador


#Variaveis globais
inimigos: list[Criatura] = []
jogadores: list[Criatura] = []


#Main
def main():
    while True:
        ready = input('Bem vindo ao Lich Boss Battle!\nDigite 1 para começar.\n')

        if ready == '1':
            print('\nVocê percorreu um longo caminho até aqui, enfrentou diversos inimigos, salvou inúmeros seres indefesos.\nE agora finalmente está de frente para ele, o General dos Mortos, Lich.')
            print()
            break
        else:
            print('\nQue pena, talvez você precise de um pouco mais de tempo para se preparar então.\n')
            return
        
    lich = Lich()
    jogador = Paladino()

    inimigos.append(lich)
    jogadores.append(jogador)

    batalha = Batalha(inimigos, jogadores)

    vencedor = batalha.iniciar()

    if isinstance(vencedor[0], Jogador):
        print('\nINCRÍVEL!!! Você conseguiu derrotar o temido Lich.\nDepois de todos os perrengues, o seu esforço deu resultados. Meus parabéns!\nVocê zerou o jogo.')
    else:
        print('\nApesar de todo o seu esforço, não foi o suficiente.\nVocê morreu, e o grande General dos Mortos sai vitorioso por mais uma era.')


#inicia a execução
if __name__ == "__main__":
    main()
