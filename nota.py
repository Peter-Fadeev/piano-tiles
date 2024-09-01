import pygame
import settings
import images
import random

class Nota:
    def __init__(self, nazvanie, dlitelnost):
        self.dlitelnost = dlitelnost
        if dlitelnost == 1:
            self.kartinka = images.KOROTKAYANENAZH
        else:
            self.kartinka = images.DLINNAYANENAZH
        self.hitbox = pygame.Rect([random.randint(0,3)*100, 0], self.kartinka.get_size())
        self.nazvanie = nazvanie
        self.zvuk = pygame.mixer.Sound("Sounds/"+nazvanie+".ogg")
        self.zvuk.set_volume(0.15)
        self.nazh = 0
    def click(self):
        if self.dlitelnost == 1:
            self.kartinka = images.KOROTKAYANAZH
        else:
            self.kartinka = images.DLINNAYANAZH
        if pygame.mixer.find_channel() == None:
            pygame.mixer.stop()
        self.zvuk.play()
        self.nazh = 1

    def otrisovka(self,window):
        window.blit(self.kartinka, self.hitbox)
    def dvizhenie(self):
        self.hitbox.y = self.hitbox.y+3
        