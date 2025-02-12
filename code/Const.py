# TAMANHO QUADRO
import pygame

WIN_WIDTH = 576
WIN_HEIGHT = 324

# COR FONTE
COLOR_ORANGE = (214, 93, 50)
COLOR_GREEN = (49, 71, 89)
COLOR_YELLOW = (255, 255, 128)
COLOR_YELLOW2 = (255, 191, 0)
COLOR_WHITE = (255, 255, 255)

# MENU DE OPÇÕES
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# VELOCIDADE DAS IMAGENS DE FUNDO
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,

    # VELOCIDADE DO PLAYER
    'Player1': 3,
    'Player2': 3,
}

# CONTROLES DOS JOGADORES
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w
                 }
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s
                   }
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a
                   }
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d
                    }
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL
                    }
