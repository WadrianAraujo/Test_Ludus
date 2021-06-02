import pygame
size = (640,640)


def ball():
    ball = pygame.image.load("assets/ball.png")
    ball_x = size[0]/2
    ball_y = size[1]/2
    ball_dy = 2.5
    ball_dx = 2.5
