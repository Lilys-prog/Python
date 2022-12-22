# Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
# o pygame é um módulo para construção de jogos. Como jogos usam música, ele também pode ser usado neste exercício
from pygame import mixer
mixer.init()
mixer.music.load('hotel.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()
while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
    if query == 'p':
        # Pausing the musice
        mixer.music.pause()
    elif query == 'r':
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
        # Stop the mixer
        mixer.music.stop()
        break






