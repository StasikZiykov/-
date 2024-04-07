import pygame
pygae.init()
screen = pygame.display.set_mode(400, 300))
pygame.draw.circle(screen, (0, 128, 255), (200, 150) 20)
pygame.display.flp()
runing = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
