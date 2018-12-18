import pygame
import sys
from pygame.locals import *

def display_regular_buttons():
    pygame.draw.rect(DISPLAYSURF, GREEN, green_button)
    pygame.draw.rect(DISPLAYSURF, RED, red_button)
    pygame.draw.rect(DISPLAYSURF, YELLOW, yellow_button)
    pygame.draw.rect(DISPLAYSURF, BLUE, blue_button)



#make some colors - RGB
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

green_button = pygame.Rect(100, 100, 300, 300)
red_button = pygame.Rect(500, 100, 300, 300)
yellow_button = pygame.Rect(100, 500, 300, 300)
blue_button = pygame.Rect(500, 500, 300, 300)

pygame.init()
FPS = 30
fps_clock = pygame.time.Clock()

width = 1000
height = 850
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simon Says!")

#background tunes
#pygame.mixer.music.load("Venus.wav")
#pygame.mixer.music.play(-1, 0)

# sound fx
#bounce_sound = pygame.mixer.Sound("Swish_4.wav")

#game loop
while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_x, mouse_y = event.pos
           the_button = which_button_was_pressed(mouse_x, mouse_y)
            
    display_regular_buttons()
    
    pygame.display.update()
    fps_clock.tick(FPS)
