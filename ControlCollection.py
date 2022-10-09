import pygame
import random
import Enemies
PLAYEROFFSET = 150


def RollSpawnPoint(size, player, screen):
    spawnPoint = pygame.Vector2(0, 0)

    # Check if the spawnpoint is too close to the player or overlaps with another enemy
    isBlocked = True
    blockedCounter = -1
    while isBlocked:
        spawnPoint.x = random.randint(0, screen.get_width())
        spawnPoint.y = random.randint(0, screen.get_height())
        blockedCounter += 1
        isBlocked = False
        if pygame.Rect.colliderect(pygame.Rect(spawnPoint.x, spawnPoint.y, size, size), pygame.Rect(player.pos.x - PLAYEROFFSET/2, player.pos.y - PLAYEROFFSET/2, player.size + PLAYEROFFSET, player.size + PLAYEROFFSET)):
            isBlocked = True
        for enemy in player.enemies:
            if pygame.Rect.colliderect(pygame.Rect(spawnPoint.x, spawnPoint.y, size, size), pygame.Rect(enemy.pos.x, enemy.pos.y, enemy.size, enemy.size)):
                isBlocked = True
    print("Spawn was blocked " + str(blockedCounter) + " times")
    return spawnPoint

def SpawnRandomEnemy(speed, color, player, dirChangeDelay):
    size = random.randint(25, 45)
    startPos = RollSpawnPoint(size, player, player.screen)
    return Enemies.RandomEnemy(startPos, size, speed, color, player, dirChangeDelay)

def SpawnChaserEnemy(speed, color, player, isVerticalChaser):
    size = random.randint(30, 40)
    startPos = RollSpawnPoint(size, player, player.screen)
    return Enemies.ChasingEnemy(startPos, size, speed, color, player, isVerticalChaser)