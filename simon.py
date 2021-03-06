# Simon-ish game

#G R
#Y B

import pygame, sys, time, random
from pygame.locals import *

def pick_random_color():
    possible_colors = ["green", "red", "yellow", "blue"]
    return random.choice(possible_colors)

def display_regular_buttons():
    pygame.draw.rect(DISPLAYSURF, GREEN, green_button)
    pygame.draw.rect(DISPLAYSURF, RED, red_button)
    pygame.draw.rect(DISPLAYSURF, YELLOW, yellow_button)
    pygame.draw.rect(DISPLAYSURF, BLUE, blue_button)

def flash_button(which_button, computer_or_human):
    if computer_or_human == "computer":
        display_regular_buttons()
        pygame.display.update()
        pygame.time.wait(250)
    if which_button == "green":
        green_sound.play()
        pygame.draw.rect(DISPLAYSURF, GREENFLASH, green_button)
    elif which_button == "red":
        red_sound.play()
        pygame.draw.rect(DISPLAYSURF, REDFLASH, red_button)
    elif which_button == "yellow":
        yellow_sound.play()
        pygame.draw.rect(DISPLAYSURF, YELLOWFLASH, yellow_button)
    elif which_button == "blue":
        blue_sound.play()
        pygame.draw.rect(DISPLAYSURF, BLUEFLASH, blue_button)
    pygame.display.update()
    pygame.time.wait(1000)

def which_button_was_pressed(x, y):
    if green_button.collidepoint( (x, y) ):
        return "green"
    elif red_button.collidepoint( (x, y) ):
        return "red"
    elif yellow_button.collidepoint( (x, y) ):
        return "yellow"
    elif blue_button.collidepoint( (x, y) ):
        return "blue"

def computer_turn():
    sequence.append( pick_random_color() )
    for the_color in sequence:
        flash_button(the_color, "computer")

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

sequence = []
user_sequence = []

#background tunes
#background_music = pygame.mixer.music.load("Mercury.wav")
#pygame.mixer.music.play(-1, 0)

#sound effects
green_sound = pygame.mixer.Sound("sfx_sounds_button5.wav")
red_sound = pygame.mixer.Sound("sfx_sounds_button6.wav")
yellow_sound = pygame.mixer.Sound("sfx_sounds_button7.wav")
blue_sound = pygame.mixer.Sound("sfx_sounds_button9.wav")

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
            flash_button(the_button, "human")
            user_sequence.append(the_button)
            print(user_sequence)
            
            # check if user entered the correct sequence
            if user_sequence == sequence:
                print("winner winner chicken dinner")
                user_sequence = []
                computer_turn()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                computer_turn()
                
        
    #DISPLAYSURF.blit(the_logo, (dvd_x, dvd_y))
    
    pygame.display.update()
    fps_clock.tick(FPS)

    