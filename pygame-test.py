import pygame
import sys
from pygame.locals import *

#make some colors - RGB
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Hey CS20!")

pygame.draw.rect(DISPLAYSURF, GREEN, (100, 50, 200, 75))

mario = pygame.image.load("mario.png")

#game loop
while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    x, y = pygame.mouse.get_pos()
    DISPLAYSURF.blit(mario, (x, y))
    pygame.display.update()