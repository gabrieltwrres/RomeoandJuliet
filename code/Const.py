# C
import pygame

COLOR_WHITE = (255, 255, 255)
C_GRAY = (140, 140, 140)
C_ORANGE = (255, 128, 0)
C_BBLUE = (26, 255, 232)
C_YELLOW = (253, 245, 12)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Lvl1BG0': 0,
    'Lvl1BG1': 0.5,
    'Lvl1BG2': 1,
    'Lvl1BG3': 2,
    'Lvl1BG4': 3,
    'Lvl1BG5': 4,
    'Lvl1BG6': 5,
    'Lvl1BG7': 6,
    'Lvl1BG8': 8,
    'Lvl2BG0': 0,
    'Lvl2BG1': 1,
    'Lvl2BG2': 2,
    'Lvl2BG3': 3,
    'Player1': 3,
    'Player1Shot': 4,
    'Player2': 3,
    'Player2Shot': 4,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 3
}

ENTITY_HEALTH = {
    'Lvl1BG0': 999,
    'Lvl1BG1': 999,
    'Lvl1BG2': 999,
    'Lvl1BG3': 999,
    'Lvl1BG4': 999,
    'Lvl1BG5': 999,
    'Lvl1BG6': 999,
    'Lvl1BG7': 999,
    'Lvl1BG8': 999,
    'Lvl2BG0': 999,
    'Lvl2BG1': 999,
    'Lvl2BG2': 999,
    'Lvl2BG3': 999,
    'Player1': 300,
    'Player2': 300,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1' : 50,
    'Enemy2': 60,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1

}

ENTITY_DEMAGE = {
    'Lvl1BG0': 0,
    'Lvl1BG1': 0,
    'Lvl1BG2': 0,
    'Lvl1BG3': 0,
    'Lvl1BG4': 0,
    'Lvl1BG5': 0,
    'Lvl1BG6': 0,
    'Lvl1BG7': 0,
    'Lvl1BG8': 0,
    'Lvl2BG0': 0,
    'Lvl2BG1': 0,
    'Lvl2BG2': 0,
    'Lvl2BG3': 0,
    'Player1': 1,
    'Player2': 1,
    'Player1Shot': 25,
    'Player2Shot': 25,
    'Enemy1' : 1,
    'Enemy2': 1,
    'Enemy1Shot': 20,
    'Enemy2Shot': 15

}

ENTITY_SCORE = {
    'Lvl1BG0': 0,
    'Lvl1BG1': 0,
    'Lvl1BG2': 0,
    'Lvl1BG3': 0,
    'Lvl1BG4': 0,
    'Lvl1BG5': 0,
    'Lvl1BG6': 0,
    'Lvl1BG7': 0,
    'Lvl1BG8': 0,
    'Lvl2BG0': 0,
    'Lvl2BG1': 0,
    'Lvl2BG2': 0,
    'Lvl2BG3': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 100,
    'Enemy2Shot': 0
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 100
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 720
WIN_HEIGHT = 405
