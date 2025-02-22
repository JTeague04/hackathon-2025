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
            image_filepath_pressed = "assets//placeholder.png"

        self.__image = pygame.transform.scale( pygame.image.load(image_filepath), (sx, sy) )
        self.__pressed_image = pygame.transform.scale( pygame.image.load(image_filepath_pressed), (sx, sy) ) # TODO Make the button scaling proper


    def get_coord(self, prcnt, string):
        if (0 <= prcnt <= 100) and (string == "x" or "y"):
            if string == "x":
                coord_x = prcnt * main.display_x
                return coord_x
            else :
                coord_y = prcnt * main.display_y
                return coord_y
        else :
            print("Invalid input to get_coord(). Please use (percentage/axis) tuple. ex : (50, x)\n")

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
