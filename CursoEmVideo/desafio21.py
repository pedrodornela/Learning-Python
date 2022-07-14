import pygame
import math
#inicializando o mixer PyGame
pygame.mixer.init()

#iniciando o PyGame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

pygame.init()
pygame.mixer.music.load('ex21a.mp3')
pygame.mixer.music.play()
pygame.event.wait()

