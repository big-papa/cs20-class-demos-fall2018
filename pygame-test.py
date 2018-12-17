import pygame
import sys
from pygame.locals import *

#make some colors - RGB
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

pygame.init()
FPS = 30
fps_clock = pygame.time.Clock()

width = 1200
height = 720
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hey CS20!")

pygame.draw.rect(DISPLAYSURF, GREEN, (100, 50, 200, 75))

mario = pygame.image.load("mario.png")
x = 200
y = 100
dx = 5
dy = 3

#game loop
while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # move mario
    x = x + dx
    y = y + dy
    
    #x, y = pygame.mouse.get_pos()
    DISPLAYSURF.blit(mario, (x, y))
    pygame.display.update()
    fps_clock.tick(FPS)