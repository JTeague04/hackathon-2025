import pygame
pygame.mixer.init()

sounds = []

# RETURNS SOUND ID FOR USAGE LATER
def loadSound(sound_filepath):
    sounds.append(pygame.mixer.Sound(sound_filepath))
    return len(sounds) - 1

def playSound(sound_id, loop_count):
    pygame.mixer.Channel(sound_id).play(sounds[sound_id], loop_count)

def stopSound(sound_id):
    pygame.mixer.Channel(sound_id).stop()

def pauseSound(sound_id):
    pygame.mixer.Channel(sound_id).pause()

def unpauseSound(sound_id):
    pygame.mixer.Channel(sound_id).unpause()