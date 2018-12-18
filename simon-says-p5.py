import pygame
import sys
from pygame.locals import *

def flash_button(which_button):
    if which_button == "green":
        green_sound.play()
        pygame.draw.rect(DISPLAYSURF, BRIGHTGREEN, green_button)
    elif which_button == "red":
        red_sound.play()
        pygame.draw.rect(DISPLAYSURF, BRIGHTRED, red_button)
    elif which_button == "yellow":
        yellow_sound.play()
        pygame.draw.rect(DISPLAYSURF, BRIGHTYELLOW, yellow_button)
    elif which_button == "blue":
        blue_sound.play()
        pygame.draw.rect(DISPLAYSURF, BRIGHTBLUE, blue_button)
    pygame.display.update()
    pygame.time.wait(1000)

def display_regular_buttons():
    pygame.draw.rect(DISPLAYSURF, GREEN, green_button)
    pygame.draw.rect(DISPLAYSURF, RED, red_button)
    pygame.draw.rect(DISPLAYSURF, YELLOW, yellow_button)
    pygame.draw.rect(DISPLAYSURF, BLUE, blue_button)

def which_button_was_pressed(x, y):
    if green_button.collidepoint( (x,y) ):
        return "green"
    elif red_button.collidepoint( (x,y) ):
        return "red"
    elif yellow_button.collidepoint( (x,y) ):
        return "yellow"
    elif blue_button.collidepoint( (x,y) ):
        return "blue"

#make some colors - RGB
RED = (150, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 150)
GREEN = (0, 150, 0)
YELLOW = (150, 150, 0)
BRIGHTRED = (255, 0, 0)
BRIGHTBLUE = (0, 0, 255)
BRIGHTGREEN = (0, 255, 0)
BRIGHTYELLOW = (255, 255, 0)

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
green_sound = pygame.mixer.Sound("sfx_sounds_button1.wav")
red_sound = pygame.mixer.Sound("sfx_sounds_button2.wav")
yellow_sound = pygame.mixer.Sound("sfx_sounds_button3.wav")
blue_sound = pygame.mixer.Sound("sfx_sounds_button4.wav")

#game loop
while True:
    DISPLAYSURF.fill(BLACK)
    display_regular_buttons()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_x, mouse_y = event.pos
           the_button = which_button_was_pressed(mouse_x, mouse_y)
           flash_button(the_button)
    
    pygame.display.update()
    fps_clock.tick(FPS)
