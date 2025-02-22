import pygame, random
from src import FrameLimiter
from src import Menus
from src import Game

# season-to-taste variables ===============================

display_x = 1920
display_y = 1080
fps = 60

# =========================================================

screen = pygame.display.set_mode((display_x, display_y))
frame_limiter = FrameLimiter.FrameLimiter(fps)

# game_state is the point in the game that we're in, ie 0 is main menu, 1 is options, 2 is driving etc
game_state = 0
inputs = []

running = True
while running:

    match game_state:
        case 0: Menus.main_menu_actions(inputs, screen)
        case 1: Menus.options_menu_actions(inputs, screen)
        case 2: Game.driving(inputs, screen)
        case 3: Game.quiz(inputs, screen)

    pygame.display.flip()
    frame_limiter.limit_frame()

    inputs = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        else:
            inputs.append(event)



