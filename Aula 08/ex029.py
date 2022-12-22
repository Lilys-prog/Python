# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
# o pygame é um módulo para construção de jogos. Como jogos usam música, ele também pode ser usado neste exercício
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('hotel.mp3')
pygame.mixer.music.play()
pygame.event.wait()






