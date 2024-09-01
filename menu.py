import images

import pygame

import settings

class Menu:
    def __init__(self,game):
        self.game = game
        self.cvet1 = [255, 255, 255]
        self.cvet2 = [0, 0, 0]
        self.cvet3 = [0, 0, 0]
        self.pesnya = 1
    def otrisovka(self):
        self.game.window.blit(images.MENUIMAGE, [0, 0])
        self.game.shrift.render_to(self.game.window, [100, 100], "в лесу родилась ёлочка", self.cvet1)
        self.game.shrift.render_to(self.game.window, [200, 300], "берёзка", self.cvet2)
        self.game.shrift.render_to(self.game.window, [220, 500], "утро", self.cvet3)
        pygame.display.update()
    def sobitiya(self):
        sobitielist = pygame.event.get()
        for sobitie in sobitielist:
            if sobitie.type == pygame.QUIT:
                self.game.gf = self.game.gf + 1
            if sobitie.type == pygame.KEYDOWN:
                if sobitie.key == pygame.K_DOWN:
                    if self.pesnya == 1:
                        self.pesnya = 2
                        self.cvet1 = [0, 0, 0]
                        self.cvet2 = [255, 255, 255]
                    elif self.pesnya == 2:
                        self.pesnya = 3
                        self.cvet2 = [0, 0, 0]
                        self.cvet3 = [255, 255, 255]
                    elif self.pesnya == 3:
                        self.pesnya = 1
                        self.cvet3 = [0, 0, 0]
                        self.cvet1 = [255, 255, 255]
                elif sobitie.key == pygame.K_UP:
                    if self.pesnya == 2:
                        self.pesnya = 1
                        self.cvet2 = [0, 0, 0]
                        self.cvet1 = [255, 255, 255]
                    elif self.pesnya == 3:
                        self.pesnya = 2
                        self.cvet3 = [0, 0, 0]
                        self.cvet2 = [255, 255, 255]
                    elif self.pesnya == 1:
                        self.pesnya = 3
                        self.cvet1 = [0, 0, 0]
                        self.cvet3 = [255, 255, 255]
                elif sobitie.key == pygame.K_RETURN:
                    self.game.menuiliigra = 1
                    self.game.winorover = 0
                    self.game.noty = []
                    self.game.numbern = 0
                    self.game.clickn = 0
                    if self.pesnya == 1:
                        self.game.songnotes = settings.CHRISTMAS_TREE_DURATION
                        self.game.songduration = settings.CHRISTMAS_TREE_DURATION
                    elif self.pesnya == 2:
                        self.game.songnotes = settings.BIRCH_NOTES
                        self.game.songduration = settings.BIRCH_DURATION
                    elif self.pesnya == 3:
                        self.game.songnotes = settings.MORNING_NOTES
                        self.game.songduration = settings.MORNING_DURATION
    def logic(self):
        pass