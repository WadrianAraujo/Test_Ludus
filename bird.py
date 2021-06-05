import pygame
import random

bird_group = [pygame.image.load("assets/Objects/bird_1.png"),
              pygame.image.load("assets/Objects/bird_1.png"),
              pygame.image.load("assets/Objects/bird_1.png"),
              pygame.image.load("assets/Objects/bird_2.png"),
              pygame.image.load("assets/Objects/bird_2.png"),
              pygame.image.load("assets/Objects/bird_3.png")
              ]


class Bird:
    def __init__(self):
        self.bird_x = random.randint(0, 640)
        self.bird_y = random.randint(40, 640)
        self.bird_dx = 5
        self.bird_dy = 5
        self.bird = bird_group[0]
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

        if self.bird_y < 40:  # Upper wall
            self.bird_y = 40
            self.bird_dy *= -1

        if self.bird_y > 620:  # Down wall
            self.bird_y = 620
            self.bird_dy *= -1

    def collider(self, body):
        rect = self.bird.get_rect(x=self.bird_x, y=self.bird_y)
        return rect.colliderect(body)
