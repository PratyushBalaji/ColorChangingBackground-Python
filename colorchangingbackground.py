import pygame

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

    r = int(254/mouseX + 1)
    g = int(254/mouseY + 1)
    b = int(254/mouseX + 1)
    color = (r,g,b)
    white = (255,255,255)
    black = (0,0,0)

    screen.fill(color)

    font = pygame.font.Font("freesansbold.ttf",48)
    text = font.render("Color : "+str(r)+', '+str(g)+', '+str(b), False, white,black)
    screen.blit(text)

    pygame.display.flip()
    clock.tick(75)