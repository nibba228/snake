import pygame as pg


class Text():
    """Класс для представления кнопки"""

    def __init__(self, screen, settings, msg):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()

        self.font = pg.font.SysFont('arial', 32, True)
        self.font_surf = self.font.render(msg, True, settings.text_colour,
         settings.surface_colour)

        self.rect = self.font_surf.get_rect()
        self.rect.center = self.screen_rect.centerx, self.screen_rect.centery

    def draw(self):
        self.screen.blit(self.font_surf, self.rect)
