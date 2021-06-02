import pygame
import random

bird_group = [pygame.image.load("assets/bird_1.png"),
              pygame.image.load("assets/bird_1.png"),
              pygame.image.load("assets/bird_1.png"),
              pygame.image.load("assets/bird_2.png"),
              pygame.image.load("assets/bird_2.png"),
              pygame.image.load("assets/bird_3.png")
              ]


class Bird:
    def __init__(self):
        self.bird_x = random.randint(0, 640)
        self.bird_y = random.randint(0, 640)
        self.bird_dx = 2.5
        self.bird_dy = 2.5
        self.bird = 0
        self.cont_image = 0

    def update(self):
        self.cont_image = (self.cont_image + 1) % 6
        self.bird = bird_group[self.cont_image]

        self.bird_y += self.bird_dy
        self.bird_x += self.bird_dx

        if self.bird_x > 620:  # Right wall
            if self.bird_y < 640:
                self.bird_x = 620
                self.bird_dx *= -1

        if self.bird_x < 0:  # Left wall
            if self.bird_y < 640:
                self.bird_x = 0
                self.bird_dx *= -1

        if self.bird_y < 0:  # Upper wall
            self.bird_y = 0
            self.bird_dy *= -1

        if self.bird_y > 620:  # Down wall
            self.bird_y = 620
            self.bird_dy *= -1

