import pygame as pg


class Link:
    """Звено змейки"""

    def __init__(self, settings, screen, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.colour = settings.snake_colour
        self.width = settings.width
        self.rect = pg.Rect(self.x, self.y, self.width, self.width)

        self.screen = screen

    def draw(self):
        self.rect = pg.Rect(self.x, self.y, self.width, self.width)
        pg.draw.rect(self.screen, self.colour, self.rect)
