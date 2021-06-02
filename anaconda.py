import random
import pygame
from pygame.locals import *
import squire

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

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((153, 51, 153))

apple_pos = on_grid_random()
apple = pygame.image.load("assets/apple.png")
apple = pygame.transform.scale(apple, (10, 10))

bird_group = [pygame.image.load("assets/bird_1.png"),
              pygame.image.load("assets/bird_1.png"),
              pygame.image.load("assets/bird_1.png"),
              pygame.image.load("assets/bird_2.png"),
              pygame.image.load("assets/bird_2.png"),
              pygame.image.load("assets/bird_3.png")
              ]

cont_image = 0

bird = pygame.image.load("assets/bird_1.png")
bird_x = random.randint(0, size[0])
bird_y = random.randint(0, size[1])
bird_dy = 2.5
bird_dx = 2.5

direction = RIGHT

clock = pygame.time.Clock()

background = pygame.image.load("assets/grass.png")


def start():
    pass


def update():
    global apple_pos, bird_y, bird_dy, bird_x, bird_dx, direction, cont_image, bird_group
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

    bird_y += bird_dy
    bird_x += bird_dx

    if bird_x > 620:  # Right wall
        if bird_y < 640:
            bird_x = 620
            bird_dx *= -1

    if bird_x < 0:  # Left wall
        if bird_y < 640:
            bird_x = 0
            bird_dx *= -1

    if bird_y < 0:  # Upper wall
        bird_y = 0
        bird_dy *= -1

    if bird_y > 620:  # Down wall
        bird_y = 620
        bird_dy *= -1

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

    cont_image = (cont_image + 1) % 6
    bird = bird_group[cont_image]

    squire.draw(background, (0, 0))
    squire.draw(apple, apple_pos)
    squire.draw(bird, (bird_x, bird_y))

    for pos in snake:
        squire.draw(snake_skin, pos)

    pygame.display.update()
