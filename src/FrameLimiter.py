import time


class FrameLimiter:

    def __init__(self, fps):
        self.__frame_start = 0
        self.__pause_time_millis = 1 / fps

    def limit_frame(self):
        delta_time = time.time() - self.__frame_start
        if delta_time < self.__pause_time_millis:
            time.sleep(self.__pause_time_millis - delta_time)
        self.__frame_start = time.time()
