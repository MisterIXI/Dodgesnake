import pygame
import math
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

from random import randint, random

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# Screen setup
width = 1400
height = 1000
playerSize = 32
screen = pygame.display.set_mode((width, height))

# Speed per Second

counter = 0

# Clock
clock = pygame.time.Clock()

# Positions
playerPos = pygame.Vector2(400, 300)
Enemy1Pos = pygame.Vector2(400, 0)

# Enemy
# enemy_01 = pygame.rect(Enemy1Pos.x, Enemy1Pos.y, playerSize, playerSize)
direction = 1
speed_x = 5
speed_y = 4
# PixelperSecond
currenttime = 0
lasttime = 0

#  GAME LOOP
running = True
while running:
    screen.fill((0, 0, 0))

# Draw Player
    pygame.draw.rect(screen, (0, 0, 250), (playerPos.x,
                     playerPos.y, playerSize, playerSize))
# Draw Enemy
    pygame.draw.rect(screen, (255, 0, 0), (Enemy1Pos.x,
                     Enemy1Pos.y, playerSize, playerSize))
# Move Enemy
    
    
    if direction == 1:
        if Enemy1Pos.x <= 0:
            direction = (direction+4)%8
        else:
            Enemy1Pos.x -= 1
    if direction == 2:
        if Enemy1Pos.x <= 0:
            direction = (direction+4)%8
        else:
            Enemy1Pos.x -= 1

        if Enemy1Pos.y <= 0:
            direction = (direction+4)%8
        else:
            Enemy1Pos.y -= 1
    if direction == 3:
        if Enemy1Pos.y <= 0:
            direction = (direction+4)%8
        else:
            Enemy1Pos.y -= 1
    if direction == 4:
        if Enemy1Pos.x >= width-playerSize:
            direction = (direction+4)%8
        else:
            Enemy1Pos.x += 1
        if Enemy1Pos.y <= 0:
            direction = (direction+4)%8
        else:
            Enemy1Pos.y -= 1
    if direction == 5:
        if Enemy1Pos.x >= width-playerSize:
            direction = (direction+4)%8
        else:
            Enemy1Pos.x += 1
    if direction == 6:
        if Enemy1Pos.x >= width-playerSize:
            direction = (direction+4)%8
        else:
            Enemy1Pos.x += 1
        if Enemy1Pos.y >= height-playerSize:
            direction = (direction+4)%8
        else:
            Enemy1Pos.y += 1
    if direction == 7:
        if Enemy1Pos.y >= width-playerSize:
            direction = (direction+4)%8
        else:
            Enemy1Pos.y += 1
    if direction == 8:
        if Enemy1Pos.x >= width-playerSize:
            direction = (direction+4)%8
        else:
            Enemy1Pos.x += 1
        if Enemy1Pos.y >= height-playerSize:
            direction = (direction+4)%8
        else:
            Enemy1Pos.y += 1


# check for keyhold
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        if playerPos.x > 0:
            playerPos.x -= 1
            if not keys[K_RIGHT]:
                counter += 1

    if keys[K_RIGHT]:
        if playerPos.x < width - playerSize:
            playerPos.x += 1
            if not keys[K_LEFT]:
                counter += 1

    if keys[K_UP]:
        if playerPos.y > 0:
            playerPos.y -= 1
            if not keys[K_DOWN]:
                counter += 1

    if keys[K_DOWN]:
        if playerPos.y < height-playerSize:
            playerPos.y += 1
            if not keys[K_UP]:
                counter += 1

    clock.tick()
    currenttime += clock.get_rawtime()
    if currenttime >= lasttime + 1000:
        lasttime = currenttime
        direction = randint(1, 8)
        # direction = randint(1,10)
        # if randint < 2:
        #     direction = randint(1, 8)

        counter = 0
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False
    textsurface = my_font.render(
        str(math.floor(counter)), False, (255, 255, 255))
    screen.blit(textsurface, (0, 0))
    # Update Screen
    pygame.display.update()