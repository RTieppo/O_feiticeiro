import pygame

def abertura():

    pygame.mixer.init()
    pygame.mixer_music.load(r'.\efeitos\abertura jogo.mp3')
    pygame.mixer_music.play(loops=1, start=0)

def botão():
    pygame.mixer.init()
    pygame.mixer_music.load(r'.\efeitos\botão.mp3')
    pygame.mixer_music.play(loops=1, start=0)