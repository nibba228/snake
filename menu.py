import pygame as pg

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.img = pg.image.load('imgs\\play_button.png')

        self.screen_rect = screen.get_rect()
        self.rect = self.img.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blit(self):
        self.screen.blit(self.img, self.rect)
