class Settings:
    """Класс для хранения общих параметров игры"""

    def __init__(self):
        self.screen_size = 500, 400
        self.screen_colour = 0, 0, 0

        self.width = 20
        self.fruit_colour = 255, 0, 0

        self.speed = self.width
        self.snake_colour = 0, 255, 0

        self.line_colour = 0, 156, 235

        self.text_colour = 0, 0, 0
        self.button_colour = 255, 255, 255
        self.button_width = self.screen_size[0] // 3
        self.button_height = self.screen_size[1] // 5
