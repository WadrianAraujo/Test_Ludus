import random
import pygame
from pygame.locals import *
import squire
import bird

size = (640, 640)


def on_grid_random():
    x = random.randint(0, size[0])
    y = random.randint(0, size[1])
    print(x)
    print(y)
    return x // 10 * 10, y // 10 * 10


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

snake = [(300, 300), (310, 300), (320, 300)]
snake_skin = pygame.Surface((20, 20))
snake_skin.fill((153, 51, 153))

apple_pos = on_grid_random()
apple = pygame.image.load("assets/apple.png")
apple = pygame.transform.scale(apple, (20, 20))
direction = RIGHT

clock = pygame.time.Clock()

background = pygame.image.load("assets/grass.png")

bird = bird.Bird()


def start():
    pass


def update():
    global apple_pos, direction
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP
            if event.key == K_DOWN:
                direction = DOWN
            if event.key == K_LEFT:
                direction = LEFT
            if event.key == K_RIGHT:
                direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    bird.update()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    squire.draw(background, (0, 0))
    squire.draw(apple, apple_pos)
    squire.draw(bird.bird, (bird.bird_x, bird.bird_y))

    for pos in snake:
        squire.draw(snake_skin, pos)

    pygame.display.update()
