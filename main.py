import pygame, random
from src import FrameLimiter
from src import Menus
from src import Game
from src import Sounds

# season-to-taste variables ===============================

display_x = 1920
display_y = 1080
fps = 60

# =========================================================

id = Sounds.loadSound("assets//sounds//random-mp3.wav")
Sounds.playSound(id, 1)

screen = pygame.display.set_mode((display_x, display_y))
frame_limiter = FrameLimiter.FrameLimiter(fps)

# game_state is the point in the game that we're in, ie 0 is main menu, 1 is options, 2 is driving etc
game_state = 0
inputs = []

running = True
while running:

    match game_state:

        case 0:
            result = Menus.main_menu_actions(inputs, screen)
            if result == Menus.MAIN_MENU_ACTIONS.EXIT:
                running = False
            elif result == Menus.MAIN_MENU_ACTIONS.GO_TO_OPTIONS:
                game_state = 1
                pygame.draw.rect(screen, "black", (0, 0, display_x, display_y))
            elif result == Menus.MAIN_MENU_ACTIONS.START:
                game_state = 2
                pygame.draw.rect(screen, "black", (0, 0, display_x, display_y))

        case 1:
            result = Menus.options_menu_actions(inputs, screen)
            if result == Menus.OPTIONS_MENU_ACTIONS.BACK:
                game_state = 0
                pygame.draw.rect(screen, "black", (0, 0, display_x, display_y))

        case 2:
            result = Game.driving(inputs, screen)
            if result == Game.DRIVING_ACTIONS.RETURN_TO_MAIN_MENU:
                game_state = 0
                pygame.draw.rect(screen, "black", (0, 0, display_x, display_y))

        case 3: Game.quiz(inputs, screen)

    pygame.display.flip()
    frame_limiter.limit_frame()

    inputs = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT or not running:
            pygame.quit()
            running = False
        else:
            inputs.append(event)



