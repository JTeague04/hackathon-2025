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

    for ychunk in range(8):
        for xchunk in range(8):

            for chunkrow in range(8):
                    for tile in range(8):
                        pygame.draw.rect(screen, "black" if chunks[ychunk*64+xchunk*8+chunkrow][tile] == 1 else "green",
                                         (x_abs+(tile*cell_size), y_abs+(chunkrow*cell_size), cell_size, cell_size))

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