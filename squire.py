import pygame
import sys

screen = None
clock = pygame.time.Clock()
fps = 60
BLACK = 0, 0, 0
size = (640, 640)
score = 0
WHITE = 255, 255, 255

def draw(surf, pos):
    screen.blit(surf, pos)


def quit():
    pygame.quit()
    exit()


def clean_screen():
    screen.fill(BLACK)


def run(scene_name):
    global fps
    fps = 60

    scene = sys.modules[scene_name]
    scene.start()
    done = False

    while not done:
        clock.tick(fps)
        done = scene.update()
        pygame.display.flip()
