# Simon-ish game

#G R
#Y B

import pygame, sys, time
from pygame.locals import *

def display_regular_buttons():
    pygame.draw.rect(DISPLAYSURF, GREEN, green_button)
    pygame.draw.rect(DISPLAYSURF, RED, red_button)
    pygame.draw.rect(DISPLAYSURF, YELLOW, yellow_button)
    pygame.draw.rect(DISPLAYSURF, BLUE, blue_button)

def flash_button(which_button):
    if which_button == "green":
        pygame.draw.rect(DISPLAYSURF, GREENFLASH, green_button)
    elif which_button == "red":
        pygame.draw.rect(DISPLAYSURF, REDFLASH, red_button)
    elif which_button == "yellow":
        pygame.draw.rect(DISPLAYSURF, YELLOWFLASH, yellow_button)
    elif which_button == "blue":
        pygame.draw.rect(DISPLAYSURF, BLUEFLASH, blue_button)
    pygame.display.update()
    pygame.time.wait(2000)

def which_button_was_pressed(x, y):
    if green_button.collidepoint( (x, y) ):
        return "green"
    elif red_button.collidepoint( (x, y) ):
        return "red"
    elif yellow_button.collidepoint( (x, y) ):
        return "yellow"
    elif blue_button.collidepoint( (x, y) ):
        return "blue"

pygame.init()

FPS = 30
fps_clock = pygame.time.Clock()

width = 1100
height = 850
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simon Says!")

#         R     G    B         
GREEN =  (0,   150,  0)
RED =    (150, 0,    0)
YELLOW = (150, 150,  0)
BLUE =   (0,   0,  150)
BLACK =  (0,   0,    0)
GREENFLASH = (0, 255, 0)
REDFLASH =   (255, 0,    0)
YELLOWFLASH =(255, 255,  0)
BLUEFLASH =  (0,   0,  255)

green_button = pygame.Rect(100, 100, 300, 300)
red_button = pygame.Rect(500, 100, 300, 300)
yellow_button = pygame.Rect(100, 500, 300, 300)
blue_button = pygame.Rect(500, 500, 300, 300)



#background tunes
#background_music = pygame.mixer.music.load("Mercury.wav")
#pygame.mixer.music.play(-1, 0)

#sound effects
#bounce_sound = pygame.mixer.Sound("swish_2.wav")

while True:
    #DISPLAYSURF.fill((255, 0, 0))
    display_regular_buttons()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            the_button = which_button_was_pressed(mouse_x, mouse_y)
            flash_button(the_button)
            #print(the_button)
            
    #DISPLAYSURF.blit(the_logo, (dvd_x, dvd_y))
    
    pygame.display.update()
    fps_clock.tick(FPS)

    