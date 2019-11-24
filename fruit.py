import pygame as pg
from random import randrange


class Fruit:

    def __init__(self, settings, screen):
        super().__init__()

        self.width = settings.width
        self.color = settings.fruit_colour
        self.settings = settings

        self.x, self.y = (randrange(0, settings.screen_size[i],
                                    self.width) for i in range(2))
        self.rect = pg.Rect(self.x, self.y, self.width, self.width)

        self.screen = screen
        self.on_screen = False

    def draw(self):
        self.rect = pg.Rect(self.x, self.y, self.width, self.width)
        pg.draw.rect(self.screen, self.color, self.rect)
        self.on_screen = True

    def update_coordinates(self):
        self.x, self.y = (randrange(0, self.settings.screen_size[i],
                                    self.width) for i in range(2))
