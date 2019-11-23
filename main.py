# TODO: съедание фрукта, счет


import pygame as pg

import game_functions as gf
from settings import Settings
from fruit import Fruit
from snake import Snake
from score import Score


def main():
    pg.init()
    settings = Settings()
    score = Score()

    screen = pg.display.set_mode(settings.screen_size)
    title = 'Snake | Max score: ' + str(score.max_score) + ' | Score: ' +\
            str(score.score)
    pg.display.set_caption(title)

    fruit = Fruit(settings, screen)
    snake = Snake(settings, screen)

    fps_controller = pg.time.Clock()

    while 1:
        gf.check_events(snake)
        gf.update(fruit, snake, score, fps_controller, screen, settings)

        if gf.game_over(snake):
            score.update_max_score()
            print('GAME OVER')
            break


main()
