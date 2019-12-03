class Settings:
    """Класс для хранения общих параметров игры"""

    def __init__(self):
        self.game_over = False
        self.fruit_on_screen = False

        self.screen_size = 500, 400
        self.screen_colour = 0, 0, 0

        self.width = 20
        self.fruit_colour = 255, 0, 0

        self.speed = self.width
        self.snake_colour = 0, 255, 0

        self.line_colour = 0, 156, 235

        self.text_colour = 0, 0, 0
        self.surface_colour = 255, 255, 255

        self.button_colour = 0, 255, 0
        self.button_width = 20

        self.menu_passed = False
        self.rect_color = 0, 0, 0
