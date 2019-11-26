import pygame as pg


class Button():
    """Класс для представления кнопки"""

    def __init__(self, screen, settings, msg):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.font = pg.font.SysFont(None, 16)
        self.font_surf = self.font.render(msg, True, settings.text_colour,
         settings.button_colour)

        self.rect = self.font_surf.get_rect()
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery

    def draw(self):
        pg.draw.rect(self.screen, self.settings.button_colour, self.rect)
