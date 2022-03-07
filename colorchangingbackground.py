import pygame
from cgitb import text
from re import S
import sys

pygame.init()
clock = pygame.time.Clock

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN,32)
pygame.display.set_caption('Color Changing Background')

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    mouseX, mouseY = pygame.mouse.get_pos()

    r = int(mouseX/7.6)
    g = int(mouseY/7.6)
    b = int(mouseX/7.6)
    if r >= 255:
        r = 255
    if g >= 255:
        g = 255
    if b >= 255:
        b = 255
    color = (r,g,b)
    white = (255,255,255)
    black = (0,0,0)

    screen.fill(color)

    font = pygame.font.Font("freesansbold.ttf",48)
    text = font.render("Color : "+str(r)+', '+str(g)+', '+str(b), False, white,black)
    screen.blit(text,(screen_width/2 - 48,screen_height-48))

    pygame.display.flip()
