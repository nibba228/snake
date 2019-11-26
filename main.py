import pygame as pg

import game_functions as gf
from settings import Settings
from fruit import Fruit
from snake import Snake
from game_stats import GameStats
from button import Button


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
    button = Button(screen, settings, 'GAME OVER')

    fps_controller = pg.time.Clock()

    while 1:
        gf.check_events(snake)
        gf.update(fruit, snake, game_stats, fps_controller, screen, settings)
        if not fruit.on_screen:
            gf.update_caption(game_stats)

        if gf.game_over(snake):
            game_stats.update_max_score()
            button.draw()
            input()
            break


main()
