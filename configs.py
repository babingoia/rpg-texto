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
        RESTAURACAO_MANA_CRITICO = 1
        MULTIPLICADOR_CRITICO = 2
        DELAY_ACAO = 3
    

    class Classes:
        """Configurações básicas de balanceamento pras classes."""

        PALADINO = { # type: ignore
            'nome': 'Paladino',
            'vida': 80,
            'mana': 0,

            'id_ataque_basico': 1,
            'dano_ataque_basico': 10,

            'id_bola_fogo': 2,
            'dano_bola_fogo': 5,

            'id_ataque_especial': 3,
            'dano_ataque_especial': 25,
            'custo_ataque_especial': 5,

            'id_recuperar_folego': 1,
            'quantidade_dados_recuperar_folego': 2,
            'restauração_mana_recuperar_folego': 1,
        }

        ASSASSINO = { # type: ignore
            'nome': 'Assassino',
            'vida': 50,
            'mana': 0,

            'id_ataque_basico': 1,
            'dano_ataque_basico': 12,
            'cura_ataque_basico': 4,
            
            'id_ataque_area': 2,
            'dano_ataque_area': 6,
            'cura_ataque_area': 2,
            
            'id_ataque_especial': 3,
            'dano_ataque_especial': 28,
            'custo_ataque_especial': 4,
        
        }
    

    class Inimigos:
        """Configurações básicas de balanceamento para os inimigos."""

        ESQUELETO = { # type: ignore
            'nome': 'esqueleto',
            'vida': 10,
            'mana': 0,
            'dano_ataque_basico': 4,
        }

        LICH = { # type: ignore
            'nome': 'Lich',
            'vida': 100,
            'mana': 0,
            'dano_ataque_basico': 10,
            'quantidade_esqueletos_invocados': 1
        }


    class Menus:
        """Constantes de configurações de menus."""

        MENU_ATAQUE = 1
        MENU_BUFFS = 2