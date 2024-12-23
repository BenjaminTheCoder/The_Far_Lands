import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 1600
WINDOWHEIGHT = 950
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('The Far Lands')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (60, 30, 0)


PLAYER_WIDTH = 32*2
PLAYER_HEIGHT = 32*2
player = pygame.Rect(300, 100, PLAYER_WIDTH, PLAYER_HEIGHT)

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 1


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            

    windowSurface.fill(GREEN)

    if moveDown and player.bottom<WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top>0:
        player.top -= MOVESPEED    
    if moveLeft and player.left>0:
        player.left -= MOVESPEED
    if moveRight and player.right<WINDOWWIDTH:
        player.right += MOVESPEED

    pygame.draw.rect(windowSurface, BLUE, player)
        
    pygame.display.update()
    mainClock.tick(10000000)
