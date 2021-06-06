import random
import pygame
from pygame.locals import *
import squire
import bird

size = (640, 640)


# Generation of ramdomized coordinates
def on_grid_random():
    x = random.randint(0, size[0]-20)
    y = random.randint(50, size[1]-20)
    return x // 15 * 15, y // 15 * 15


# Collision
def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Sounds
eat = pygame.mixer.Sound("assets/Sounds/eat.wav")

# Generation snake
snake = [(300, 300), (315, 300), (330, 300)]
snake_head = pygame.image.load('assets/Objects/head_snake.png')
snake_heads = [pygame.transform.rotate(snake_head, 180),
               pygame.transform.rotate(snake_head, 90),
               snake_head,
               pygame.transform.rotate(snake_head, -90)]
snake_body = pygame.image.load('assets/Objects/body_snake.png')
snake_skin = pygame.Surface((15, 15))
snake_skin.fill((153, 51, 153))

# Generation snake
apple_pos = on_grid_random()
apple = pygame.image.load("assets/Objects/apple.png")
apple = pygame.transform.scale(apple, (15, 15))
direction = RIGHT

# Definition assets
background = pygame.image.load("assets/Background/grass.png")
bar = pygame.image.load("assets/Background/bar.png")
font = pygame.font.Font('assets/PressStart2P.ttf', 20)


score = 0
bird_cont = 1
clock = pygame.time.Clock()
bird_list = []
aux = 5
bird_list.append(bird.Bird())


def start():
    global snake, apple_pos, score, bird_cont, bird_list, aux
    snake = [(300, 300), (315, 300), (320, 300)]
    apple_pos = on_grid_random()
    score = 0
    bird_cont = 1
    pygame.mixer.music.load('assets/Sounds/background_game.wav')
    pygame.mixer.music.play(-1)
    bird_list = [bird.Bird()]
    aux = 5
    pass


def update():
    global score, apple_pos, direction, bird_cont, aux
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        # Game keys
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP
            if event.key == K_DOWN:
                direction = DOWN
            if event.key == K_LEFT:
                direction = LEFT
            if event.key == K_RIGHT:
                direction = RIGHT

    # Collision snake with apple
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))
        score += 1
        eat.play()

    # Bird class call
    for i in range(len(bird_list)):
        bird_list[i].update()

    # Score point
    if score == aux:
        aux += 5
        bird_list.append(bird.Bird())

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 15)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 15)
    if direction == LEFT:
        snake[0] = (snake[0][0] - 15, snake[0][1])
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 15, snake[0][1])

    # Collision snake with wall's
    if snake[0][0] >= 640 or snake[0][1] >= 640 or snake[0][0] < 0 or snake[0][1] < 40:
        squire.run("gameover")
        start()
        pygame.mixer.music.stop()

    # Collision snake
    for i in range(1, len(snake)-1):
        for j in bird_list:
            if j.collider(snake_body.get_rect(topleft=snake[i])):
                squire.run("gameover")
                start()
                pygame.mixer.music.stop()

        if collision(snake[0], snake[i]):
            squire.run("gameover")
            start()
            pygame.mixer.music.stop()

    # Generation score
    score_text = font.render('SCORE: {}'.format(score), True, squire.BLACK)
    bird_cont_text = font.render('NIVEL: {}'.format(bird_cont), True, squire.BLACK)

    # Draw elements of game
    squire.clean_screen()
    squire.draw(background, (0, 0))
    squire.draw(apple, apple_pos)
    squire.draw(bar, (0, 0))
    squire.draw(score_text, (10, 10))
    squire.draw(bird_cont_text, (320, 10))
    squire.draw(snake_heads[direction], snake[0])

    for i in range(len(bird_list)):
        squire.draw(bird_list[i].bird, (bird_list[i].bird_x, bird_list[i].bird_y))

    for i in range(1, len(snake)):
        squire.draw(snake_body, snake[i])
