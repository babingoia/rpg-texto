#Configurações específicas de inimigos.
#libs


#Classes
class ESQUELETO():
    """Configurações da classe Esqueleto."""

    STATUS = ConfiguracaoStatus()
    ATAQUE_BASICO = ConfiguracaoBasicaAtaque()

    STATUS.NOME= 'esqueleto'
    STATUS.VIDA= 10

    ATAQUE_BASICO.MULTIPLICADOR_CRITICO = Combate.MULTIPLICADOR_CRITICO_PADRAO

    ATAQUE_BASICO.ID = 1
    ATAQUE_BASICO.DANO = 4

    #Mensagens
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_CRITICO = f'\nELE TE ACERTA EM CHEIO!!!\n'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_FALHA = f'\nVocê consegue desviar do ataque a tempo!'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_INICIO = f'\nO esqueleto corre em sua direção com a espada levantada...'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_NORMAL = f'\nEle te corta.\n'


class LICH():
    """Configuroções da classe de Lich."""

    STATUS = ConfiguracaoStatus()
    ATAQUE_BASICO = ConfiguracaoBasicaAtaque()
    INVOCAR_ESQUELETO = ConfiguracaoInvocacao()


    STATUS.NOME = 'Lich'
    STATUS.VIDA = 100
    ATAQUE_BASICO.MULTIPLICADOR_CRITICO = Combate.MULTIPLICADOR_CRITICO_PADRAO

    #IDs
    ATAQUE_BASICO.ID = 1
    INVOCAR_ESQUELETO.ID = 2

    #Danos
    ATAQUE_BASICO.DANO = 10
    INVOCAR_ESQUELETO.QUANTIDADE_INVOCACOES = 1
    INVOCAR_ESQUELETO.QUANTIDADE_INVOCACOES_CRITICO = 2

    #Mensagens
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_INICIO = f'\nO Lich levanta suas mãos, invocando um raio necromante...'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_FALHA = f'\nVocê consegue desviar da magia a tempo!'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_NORMAL = f'\nEle acerta o raio em você.\n'
    ATAQUE_BASICO.MENSAGENS.MENSAGEM_CRITICO = f'\nELE TE ACERTA EM CHEIO!!!\n'

    INVOCAR_ESQUELETO.MENSAGENS.MENSAGEM_INICIO = f'\n O Lich toca na terra, fazendo-a tremer...'
    INVOCAR_ESQUELETO.MENSAGENS.MENSAGEM_FALHA = f'\n Nada acontece'
    INVOCAR_ESQUELETO.MENSAGENS.MENSAGEM_NORMAL = f'\n esqueleto surge da terra.'
    INVOCAR_ESQUELETO.MENSAGENS.MENSAGEM_CRITICO = f'\n esqueletos surgem da terra!'
    