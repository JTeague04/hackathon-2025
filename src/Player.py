import time
from src import Options


class Player:

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__last_moved = 0

        self.__direction = 0 # 0-7 N, NE, E and so on
        self.__momentum = 0

        self.__throttle_held = False
        self.__on_grass = False

    def press_throttle(self):
        self.__throttle_held = True
    def release_throttle(self):
        self.__throttle_held = False

    def on_grass(self):
        self.__on_grass = True
    def off_grass(self):
        self.__on_grass = False

    def set_direction(self, direction):
        self.__direction = direction

    def try_move(self):

        if not (time.time() - self.__last_moved > Options.CAR_MOVEMENT_DELAY * (1.41 if self.__direction %2 == 1 else 1)):
            return

        self.__last_moved = time.time()
        match self.__direction:
            case 0:
                self.__x += 0
                self.__y -= 1
            case 1:
                self.__x += 1
                self.__y -= 1
            case 2:
                self.__x += 1
            case 3:
                self.__x += 1
                self.__y += 1
            case 4:
                self.__y += 1
            case 5:
                self.__x -= 1
                self.__y += 1
            case 6:
                self.__x -= 1
            case 7:
                self.__x -= 1
                self.__y -= 1

