import pygame

a = True
pygame.init()
pygame.mixer.music.load("/usr/share/sounds/alsa/Front_Center.wav")
while a == True:
    pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue