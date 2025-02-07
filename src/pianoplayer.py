import pygame
from .constants import *

class PianoPlayer(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            raise Exception("PianoPlayer not assigned a container")
        print(MID_KEYBOARD)
        pygame.mixer.init()
        #self.keyboard = {"C4": pygame.mixer.Sound("src/C4.wav")}
        self.keyboard = pygame.mixer.Sound("src/C4.wav")

    def draw(self, screen):
        pass

    def play_key(self):
    #self.keyboard["C4"].play()
        self.keyboard.play()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.play_key()
            return
        # If nothing, begin fadeout
        self.keyboard.fadeout(FADEOUT_TIME)

