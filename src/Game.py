from src import Road
import pygame

class DRIVING_ACTIONS:
    NONE = 0
    RETURN_TO_MAIN_MENU = 1

def driving(events, screen):

    road = Road.Road()

    for i in range(8):
        road.generate_chunk(i)

    cell_size = 10
    chunks = road.get_roads()

    x_abs = 0
    y_abs = 0

    for imagey in range(8):
        for imagex in range(8):

            for pixely in range(8):
                    for pixelx in range(8):
                        pygame.draw.rect(screen, "black" if chunks[imagey*64+imagex*8+pixely][pixelx] == 1 else "green",
                                         (imagex*cell_size*8 + cell_size*pixelx,
                                          cell_size*pixely +y_abs, cell_size, cell_size))

            x_abs += 8*cell_size
        y_abs += 8*cell_size

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return DRIVING_ACTIONS.RETURN_TO_MAIN_MENU

    pygame.display.flip()
    return DRIVING_ACTIONS.NONE

def quiz(events, screen):
    pass