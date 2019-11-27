import pygame as pg


class RestartButton:
    """Класс для кнорки перезапуска игры"""

    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.image = pg.image.load('imgs\\restart_button.png.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.centerx, self.screen_rect.centery + 60
        self.rect.width = settings.button_width

    def blit(self):
        self.screen.blit(self.image, self.rect)
