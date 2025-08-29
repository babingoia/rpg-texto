#Inicia o programa
# Libs
from interfaces import ICriatura, DataFactory
from views import ViewFactory
from models import FactoryCriatura
from controllers import Batalha, AtaqueStrategyFactory


#Variaveis globais
inimigos: list[ICriatura] = []
jogadores: list[ICriatura] = []
criatura_factory = FactoryCriatura()

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
        
    lich = criatura_factory.criar('lich')
    jogador = criatura_factory.criar('paladino')

    inimigos.append(lich)
    jogadores.append(jogador)

    batalha = Batalha(ViewFactory(), DataFactory(), jogadores, inimigos, AtaqueStrategyFactory())

    vencedor = batalha.iniciar()

    if vencedor == 'jogador':
        print('\nINCRÍVEL!!! Você conseguiu derrotar o temido Lich.\nDepois de todos os perrengues, o seu esforço deu resultados. Meus parabéns!\nVocê zerou o jogo.')
    else:
        print('\nApesar de todo o seu esforço, não foi o suficiente.\nVocê morreu, e o grande General dos Mortos sai vitorioso por mais uma era.')


#inicia a execução
if __name__ == "__main__":
    main()
