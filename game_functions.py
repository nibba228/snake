import pygame as pg
from link import Link
from score import Score


def check_events(snake):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            check_keydown_events(event, snake)


def check_keydown_events(event, snake):
    if event.key == pg.K_q:
        exit()
    if event.key == pg.K_RIGHT:
        snake.change_to = 'right'
    if event.key == pg.K_LEFT:
        snake.change_to = 'left'
    if event.key == pg.K_UP:
        snake.change_to = 'up'
    if event.key == pg.K_DOWN:
        snake.change_to = 'down'


def update(fruit, snake, score, fps_controller, screen, settings):
    snake.update()

    screen.fill((255, 255, 255))
    fruit.on_screen = False

    if not fruit.on_screen:
        fruit.draw()
    snake.draw()

    check_fruit_collisions(snake, fruit, settings, screen, score)

    line_up_screen(screen, settings)
    pg.display.flip()
    fps_controller.tick(17)

    if not fruit.on_screen:
        update_caption(score)


def check_fruit_collisions(snake, fruit, settings, screen, score):
    last_element = snake.links[-1]
    if snake.head.rect.top == fruit.rect.top and snake.head.x == fruit.x:
        snake.links.append(Link(settings, screen, last_element.x,
                           last_element.y - settings.speed))
        fruit.update_coordinates()
        score.add_score()
        fruit.on_screen = False


def game_over(snake):
    for link in snake.links[1:]:
        if snake.head.rect.top == link.rect.top and snake.head.x == link.x:
            return True
    return False


def update_caption(score):
    pg.display.set_caption('Snake | Max score: ' + str(score.max_score) +
                           ' | Score: ' + str(score.score))


def line_up_screen(screen, settings):
    _draw_horizontal_lines(screen, settings)
    _draw_vertical_lines(screen, settings)


def _draw_vertical_lines(screen, settings):
    y0, y1 = 0, settings.screen_size[1]
    for x in range(0, settings.screen_size[0] + 1, settings.width):
        pg.draw.line(screen, settings.line_colour, (x, y0), (x, y1))


def _draw_horizontal_lines(screen, settings):
    x0, x1 = 0, settings.screen_size[0]
    for y in range(0, settings.screen_size[1] + 1, settings.width):
        pg.draw.line(screen, settings.line_colour, (x0, y), (x1, y))
