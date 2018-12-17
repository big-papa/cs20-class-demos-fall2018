import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fps_clock = pygame.time.Clock()

width = 1100
height = 850
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello CS20!")


pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (300, 100, 200, 50))

# loading image
the_logo = pygame.image.load("dvd-logo.png")
dvd_width = the_logo.get_width()
dvd_height = the_logo.get_height()
dvd_x = 100
dvd_y = 100
dx = 5
dy = 3

#background tunes
background_music = pygame.mixer.music.load("Mercury.wav")
pygame.mixer.music.play(-1, 0)

#sound effects
bounce_sound = pygame.mixer.Sound("swish_2.wav")

while True:
    DISPLAYSURF.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    DISPLAYSURF.blit(the_logo, (dvd_x, dvd_y))
    
    dvd_x += dx
    dvd_y += dy
    
    if dvd_x + dvd_width > width or dvd_x < 0:
        dx = dx * -1
        bounce_sound.play()
    if dvd_y + dvd_height > height or dvd_y < 0:
        dy = dy * -1
        bounce_sound.play()
    
    pygame.display.update()
    fps_clock.tick(FPS)

