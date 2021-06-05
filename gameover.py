import pygame
import squire
import anaconda
score = anaconda.score

sound_gor = pygame.mixer.Sound('assets/Sounds/game_over.wav')
background = pygame.image.load('assets/Background/gameover_background.jpg')
background_rect = background.get_rect(center=(320, 320))





font = pygame.font.Font('assets/PressStart2P.ttf', 12)
replay_text = font.render('RESTART', True, squire.WHITE)
replay_rect = replay_text.get_rect(center=(320, 415))
menu_text = font.render('MENU', True, squire.WHITE)
menu_rect = menu_text.get_rect(center=(320, 462))
quit_text = font.render('QUIT', True, squire.WHITE)
quit_rect = menu_text.get_rect(center=(320, 510))


def start():
    sound_gor.play()
    pass


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    score_font = pygame.font.Font('assets/PressStart2P.ttf', 30)
    score_text = score_font.render("SCORE: {}".format(anaconda.score), True, squire.WHITE)
    score_rect = score_text.get_rect(center=(320, 100))
    print(anaconda.score)
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if replay_rect.collidepoint(pos):
            squire.run('anaconda')

        elif menu_rect.collidepoint(pos):
            pygame.mixer.music.load("assets/Sounds/background_ini.mp3")
            pygame.mixer.music.play(-1)
            squire.run('menu')
            #return True

        elif quit_rect.collidepoint(pos):
            squire.quit()

    squire.clean_screen()
    squire.draw(background, background_rect)
    squire.draw(score_text, score_rect)
    squire.draw(replay_text, replay_rect)
    squire.draw(menu_text, menu_rect)
    squire.draw(quit_text, quit_rect)
