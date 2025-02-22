import pygame
from pathlib import Path


class Button:

    def __init__(self, x, y, sx, sy, image_filepath, image_filepath_pressed):
        # Defined
        self.__x = x
        self.__y = y
        self.__sx = sx
        self.__sy = sy

        self.__pressed = False

        # Load the button image
        if not Path(image_filepath).is_file():
            image_filepath = "assets//placeholder.png"
        if not Path(image_filepath_pressed).is_file():
            image_filepath = "assets//placeholder.png"

        self.__image = pygame.image.load(image_filepath)
        self.__pressed_image = pygame.image.load(image_filepath_pressed)

    def get_image(self):
        if self.__pressed:
            return self.__pressed_image
        return self.__image

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def set_pressed(self, pressed):
        self.__pressed = pressed

    def collides_with(self, x, y):
        return self.__x <= x <= self.__x + self.__sx and self.__y <= y <= self.__y + self.__sy
