import pygame

pygame.init()

import squire
import anaconda
import bird
import menu
import gameover

squire.screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("ANACONDA POWER")

squire.run('menu')

pygame.quit()
