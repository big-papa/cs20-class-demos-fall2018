import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hello CS20!")


pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (300, 100, 200, 50))

# loading image
the_logo = pygame.image.load("dvd-logo.png")
dvd_x = 100
dvd_y = 100


while True:
    DISPLAYSURF.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    DISPLAYSURF.blit(the_logo, (dvd_x, dvd_y))
    
    dvd_x += 0.1
    dvd_y -= 0.1
    
    pygame.display.update()

