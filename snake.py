from random import randrange

from link import Link


class Snake:

    def __init__(self, settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.speed = settings.speed
        self.colour = settings.snake_colour

        self.start_x, self.start_y = (randrange(0, settings.screen_size[0],
                                      settings.width) for _ in range(2))

        self.head = Link(settings, screen, self.start_x, self.start_y)
        self.links = [self.head] + [
            Link(settings, screen, self.head.x, self.head.y - self.speed * i)
            for i in range(1, 3)
        ]

        self.direction = 'right'
        self.change_to = ''

    def draw(self):
        for link in self.links:
            link.draw()

    def update(self):
        self.check_edges()
        self.validate_direction_and_change()

        if self.direction == 'up':
            self.move()
            self.head.y -= self.speed
        if self.direction == 'down':
            self.move()
            self.head.y += self.speed
        if self.direction == 'right':
            self.move()
            self.head.x += self.speed
        if self.direction == 'left':
            self.move()
            self.head.x -= self.speed

    def move(self):
        step = 2
        length = len(self.links)
        for link in reversed(self.links[1:]):
            link.x, link.y = self.links[length - step].x,\
                             self.links[length - step].y
            step += 1

    def validate_direction_and_change(self):
        if any((self.change_to == "right" and not self.direction == "left",
                self.change_to == "left" and not self.direction == "right",
                self.change_to == "up" and not self.direction == "down",
                self.change_to == "down" and not self.direction == "up")):
            self.direction = self.change_to

    def check_edges(self):
        if self.head.x > self.settings.screen_size[0]:
            self.head.x = 0
        elif self.head.x < 0:
            self.head.x = self.settings.screen_size[0]
        elif self.head.y > self.settings.screen_size[1]:
            self.head.y = 0
        elif self.head.y < 0:
            self.head.y = self.settings.screen_size[1]
