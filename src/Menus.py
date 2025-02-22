import pygame
from src import Button
from src import Options

MAIN_MENU = (
    Button.Button(50, 50, 50, 50, "assets//buttons//exit.png"),
    Button.Button(100, 100, 100, 100, "assets//buttons//start.png"),
    Button.Button(100, 100, 100, 100, "assets//buttons//options.png")
)
OPTIONS_MENU = (
    Button.Button(50, 50, 50, 50, "assets//buttons//back.png"),
    Button.Button(150, 100, 100, 100, "assets//buttons//volume_up.png"),
    Button.Button(300, 100, 100, 100, "assets//buttons//volume_down.png")
)

class MAIN_MENU_ACTIONS:
    NONE = 0
    EXIT = 1
    START = 2
    GO_TO_OPTIONS = 3

class OPTIONS_MENU_ACTIONS:
    NONE = 0
    BACK = 1

def main_menu_actions(events, screen):

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for index, button in enumerate(MAIN_MENU):
                if button.collides_with(mouse_pos[0], mouse_pos[1]):
                    return index+1

    for button in MAIN_MENU:
        screen.blit(button.get_image(), (button.get_x(), button.get_y()) )

    return MAIN_MENU_ACTIONS.NONE

def options_menu_actions(events, screen):

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            for index, button in enumerate(MAIN_MENU):
                if button.collides_with(mouse_pos[0], mouse_pos[1]):

                    if index == 0:
                        return OPTIONS_MENU_ACTIONS.BACK

                    # Edit the clicked option (in order of the buttons as they're defined above)
                    if index == 1:
                        if Options.MASTER_VOLUME != 10:
                            Options.MASTER_VOLUME += 1
                            print(Options.MASTER_VOLUME)
                    elif index == 2:
                        if Options.MASTER_VOLUME != 0:
                            Options.MASTER_VOLUME -= 1
                            print(Options.MASTER_VOLUME)

    return OPTIONS_MENU_ACTIONS.NONE
