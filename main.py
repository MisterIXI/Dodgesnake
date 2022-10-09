import pygame
import math

import Player
import Enemies
import ControlCollection as cc
import Spawner
import UI

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
scoreLabel = my_font.render("Score: 0", False, (255, 255, 255))
spawnCountdown = my_font.render("Next wave in: 10", False, (255, 255, 255))
clock = pygame.time.Clock()

# Setup the screen
screen_width = 1400
screen_height = 800
playersize = 32
playerPos = pygame.Vector2(screen_width/2 - playersize/2, screen_height/2 - playersize/2)
screen = pygame.display.set_mode((screen_width, screen_height))

# Title and Icon
pygame.display.set_caption("Dodgesnake")

# Create Player rectangle
player = Player.Character(playerPos, playersize, 3, (255, 255, 255), screen)
spawner = Spawner.Spawner(clock, player)
gui = UI.GameOverlay(spawner, screen)

# enemy = Enemies.RandomEnemy(pygame.Vector2(0, 0), 32, 5, (255, 0, 0), player, 150)
running = True
def gameLoop():
    global running
    while running:
        screen.fill((74, 74, 74))
        clock.tick()
        spawner.tick(clock.get_time())
        if not player.tick(clock.get_time()):
            running = False
        for enemy in player.enemies:
            enemy.tick(clock.get_time())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()
        gui.tick(clock.get_time())
        pygame.display.update()
if running:
    gameLoop()
pygame.event.clear()
while True:
    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
            break
        if event.key == pygame.K_r:
            player.enemies.clear()
            spawner.reset()
            gui.reset()
            running = True
            clock.tick()
            gameLoop()
    if event.type == pygame.QUIT:
        pygame.quit()

