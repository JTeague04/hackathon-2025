import pygame, random

display_x, display_y = 1920, 1080
point_count = 20

screen = pygame.display.set_mode((display_x, display_y))

connection_points = [
    [random.randint(0, display_x), random.randint(0, display_y)] for _ in range(point_count)
]
connection_lines = [
    [random.randint(0, point_count) for _ in range(3)] for point in range(point_count)
]

for point in connection_points:
    pygame.draw.rect(screen, "white", (point[0], point[1], 2, 2))

    # Pick some random connections

pygame.display.flip()

input()