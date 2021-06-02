import pygame
import squire

#pygame.mixer.music.load("assets/background_ini.mp3")
#pygame.mixer.music.play(-1)

background = pygame.image.load('assets/grass.png')

title_font = pygame.font.Font('assets/PressStart2P.ttf', 30)
title_text = title_font.render('Anaconda', True, squire.BLACK)
title_rect = title_text.get_rect(center=(330, 205))

font = pygame.font.Font('assets/PressStart2P.ttf', 18)
play_text = font.render('play', True, squire.BLACK)
play_rect = play_text.get_rect(center=(330, 307))
credits_text = font.render('credits', True, squire.BLACK)
credits_rect = credits_text.get_rect(center=(330, 370))
quit_text = font.render('quit', True, squire.BLACK)
quit_rect = quit_text.get_rect(center=(330, 433))


def start():
    pass


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            squire.quit()

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if play_rect.collidepoint(pos):
            squire.run('anaconda')
            squire.run('gameover')
        elif credits_rect.collidepoint(pos):
            squire.run('credits')
        elif quit_rect.collidepoint(pos):
            squire.quit()

   # squire.clear_screen()
    squire.draw(background, (0, 0))
    squire.draw(title_text, title_rect)
    squire.draw(play_text, play_rect)
    squire.draw(credits_text, credits_rect)
    squire.draw(quit_text, quit_rect)
