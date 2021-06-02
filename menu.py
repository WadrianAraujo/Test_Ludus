import pygame
import squire

#pygame.mixer.music.load("assets/background_ini.mp3")
#pygame.mixer.music.play(-1)

background = pygame.image.load('assets/grass.png')
title = pygame.image.load('assets/title.png')
title = pygame.transform.scale(title, (350, 60))
start_button = pygame.image.load('assets/start.png')
quit_button = pygame.image.load('assets/quit.png')

start_rect = start_button.get_rect(center=(320, 307))
quit_rect = quit_button.get_rect(center=(320, 350))

font_creator = pygame.font.Font('assets/PressStart2P.ttf', 15)
font = pygame.font.Font('assets/PressStart2P.ttf', 18)
credits_text = font_creator.render('by: Mortarion(Wadrian Araujo)', True, squire.BLACK)


def start():
    pass


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            squire.quit()

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if start_rect.collidepoint(pos):
            squire.run('anaconda')
            squire.run('gameover')

        elif quit_rect.collidepoint(pos):
            squire.quit()

    squire.draw(background, (0, 0))
    squire.draw(title, (150, 120))
    squire.draw(start_button, (250, 277))
    squire.draw(quit_button, (250, 350))
