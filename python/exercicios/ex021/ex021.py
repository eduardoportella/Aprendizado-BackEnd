import p
pygame.mixer.init()
pygame.mixer.music.load('SAY POZE - LEOD.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass