import pygame as pg
from time import sleep

import game_functions as gf
from settings import Settings
from fruit import Fruit
from snake import Snake
from game_stats import GameStats
from text import Text
from restart_button import RestartButton


def main():
    pg.init()
    settings = Settings()
    game_stats = GameStats()

    screen = pg.display.set_mode(settings.screen_size)
    title = 'Snake | Max score: ' + str(game_stats.max_score) + ' | Score: ' +\
            str(game_stats.score)
    pg.display.set_caption(title)

    fruit = Fruit(settings, screen)
    snake = Snake(settings, screen)
    text = Text(screen, settings, 'GAME OVER')
    button = RestartButton(screen, settings)

    fps_controller = pg.time.Clock()

    while 1:
        if not settings.game_over:
            gf.check_events(snake)
            gf.update(fruit, snake, game_stats, fps_controller, screen, settings)

            if not settings.fruit_on_screen:
                gf.update_caption(game_stats)

            gf.check_game_over(snake, settings)
        else:
            game_stats.update_max_score()
            text.draw()
            button.blit()
            pg.display.flip()

            if gf.is_button_pressed(button, settings):
                gf.restart_game(game_stats, snake, fruit, settings, screen)
                snake = Snake(settings, screen)
                fruit = Fruit(settings, screen)


main()
