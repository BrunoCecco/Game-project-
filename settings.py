import pygame as pg

pg.init()

# define colours

COLOR_INACTIVE = (0, 100, 0)
COLOR_ACTIVE = (0, 200, 0)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HOVER_COLOR = (50, 50, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
LIGHTGREY = (100, 100, 100)
DARKGREY = (40, 40, 40)
RED = (245, 50, 17)

# project game settings/options

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 420
FONT = pg.font.Font(None, 32)

HS_file = "highscore.txt"
HS_name = "hs_name.txt"
Coins_file = "coins.txt"
game_speed = 4

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # create screen 
pg.display.set_caption("Project game")



