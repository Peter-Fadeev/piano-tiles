import time

import settings
import nota
import menu

import pygame as pg
import random

import pygame.freetype

pg.init()
pg.mixer.init()


class Game:
    def __init__(self):
        self.window = pg.display.set_mode(settings.SIZE)
        self.gf = 100
        self.chasy = pg.time.Clock()
        self.noty = []
        self.sobitienota = pg.USEREVENT
        pg.time.set_timer(self.sobitienota, 500)
        self.numbern = 0
        self.clickn = 0
        self.shrift = pygame.freetype.Font("53e59-muller-extrabold-demo.ttf", 24)
        self.winorover = 0
        self.menu = menu.Menu(self)
        self.menuiliigra = 1
        self.moment = 0
        self.songnotes = settings.CHRISTMAS_TREE_NOTES
        self.songduration = settings.CHRISTMAS_TREE_DURATION

    def sobitiya(self):
        sobitielist = pg.event.get()
        for sobitie in sobitielist:
            if sobitie.type == pg.QUIT:
                self.gf = self.gf + 1
            if sobitie.type == self.sobitienota and self.numbern < len(self.songnotes):
                self.nota = nota.Nota(self.songnotes[self.numbern], self.songduration[self.numbern])
                self.numbern = self.numbern + 1
                self.noty.append(self.nota)
            if sobitie.type == pg.MOUSEBUTTONDOWN:
                for n in self.noty:
                    if n.hitbox.collidepoint(sobitie.pos) == True and n.nazh == 0:
                        numbern = self.noty.index(n)
                        if numbern == self.clickn:
                            n.click()
                            self.clickn = self.clickn + 1
                        else:
                            self.winorover = 1
                            self.moment = pg.time.get_ticks()
                            


    def otrisovka(self):
        self.window.fill([255, 255, 255])
        if self.winorover == 0:
            for n in self.noty:
                n.otrisovka(self.window)
        else:
            self.shrift.render_to(self.window, [130, 200], "проигрыш")
        x = settings.ODINSTOLB
        gf = 0
        fg = settings.KOLSTOLB
        while gf != fg:
            pg.draw.line(self.window, [0, 0, 0], [x, 0], [x, 600])
            x = x+settings.ODINSTOLB
            gf = gf+1
        self.shrift.render_to(self.window, [10, 50], "нажато " + str(self.clickn) + " нот" )
        self.shrift.render_to(self.window, [205, 50], "осталось " +str(len(self.songnotes) - self.clickn) + " нот")
        pg.draw.line(self.window, [255, 0, 0], [0, 500], [400, 500])
        if self.clickn == len(self.songnotes) and self.noty[-1].hitbox.y > 500:
            self.shrift.render_to(self.window, [125, 250], "победа")
        pg.display.update()
        

    def logic(self):
        if self.winorover == 0: 
            for n in self.noty:
                n.dvizhenie()
                if n.hitbox.y > 500 and n.nazh == 0:
                    self.winorover = 1
                    self.moment = pg.time.get_ticks()
                    self.noty = []
        if pygame.time.get_ticks() - self.moment > 2000 and self.winorover == 1:
            self.menuiliigra = 0
        
    def startgame(self):   
        while self.gf == 100:
            if self.menuiliigra == 1:
                self.sobitiya()
                self.otrisovka()
                self.logic()
            else:
                self.menu.sobitiya()
                self.menu.otrisovka()
                self.menu.logic()
            self.chasy.tick(120)
            

obj = Game()
obj.startgame()