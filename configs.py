#Lib com as constantes e configurações do projeto
#Libs


#Classes
class Configuracoes:
    """Biblioteca que guarda as configurações do projeto."""
    
    class Cores:
        """Subbiblioteca com as cores"""
        YELLOW = '\033[93m'
        RESET = '\033[0m'
    

    class Dados:
        """Subblioteca com os tipos de dados do projeto."""

        D2 = 2
        D4 = 4
        D6 = 6
        D8 = 8
        D10 = 10
        D12 = 12
        D20 = 20

    
    class Combate:
        """Guarda alguns valores especificos e importantes para combate."""

        FALHA = 1
        CRITICO = 6
        DELAY_ACAO = 3
    

    class Classes:
        """Configurações básicas de balanceamento pras classes."""

        PALADINO = { # type: ignore
            'nome': 'Paladino',
            'vida': 80,
            'mana': 0
        }

        ASSASSINO = { # type: ignore
            'nome': 'Assassino',
            'vida': 50,
            'mana': 0
        
        }
    

    class Inimigos:
        """Configurações básicas de balanceamento para os inimigos."""

        ESQUELETO = { # type: ignore
            'nome': 'esqueleto',
            'vida': 10,
            'mana': 0
        }

        LICH = { # type: ignore
            'nome': 'Lich',
            'vida': 100,
            'mana': 0
        }