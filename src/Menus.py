import pygame
from src import Button
from src import Options

LOGO = pygame.transform.scale( pygame.image.load("assets//logo.png"), (1200, 400) )
MAIN_MENU = (
    Button.Button(25, 25, 100, 100, "assets//buttons//exit_normal.png", "assets//buttons//exit_depressed.png"),
    Button.Button(300, 800, 250, 250, "assets//buttons//start_normal.png", "assets//buttons//start_depressed.png"),
    Button.Button(600, 800, 250, 250, "assets//buttons//options_normal.png", "assets//buttons//options_depressed.png")
)
OPTIONS_MENU = (
    Button.Button(50, 50, 50, 50, "assets//buttons//back.png", "assets//buttons//back.png"),
    Button.Button(50, 150, 100, 100, "assets//buttons//volume_up.png", "assets//buttons//volume_up.png"),
    Button.Button(50, 300, 100, 100, "assets//buttons//volume_down.png", "assets//buttons//volume_down.png"),
    Button.Button(50, 450, 100, 100, "assets//buttons//rand1.png", "assets//buttons//rand1.png")

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

    screen.blit(LOGO, (360, 100))

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

    for button in OPTIONS_MENU:
        screen.blit(button.get_image(), (button.get_x(), button.get_y()) )

    return OPTIONS_MENU_ACTIONS.NONE
