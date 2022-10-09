import pygame
import ControlCollection as cc

class Spawner():
    def __init__(self, clock, player):
        self.player = player
        self.spawnDelay = 0
        self.spawnCounter = 0
        self.finishedSpawning = False
    
    def reset(self):
        self.spawnCounter = 0
        self.spawnDelay = 0

    def tick(self, clockTick):
        if self.finishedSpawning:
            return
        self.spawnDelay -= clockTick
        if self.spawnDelay <= 0:
            self.spawnDelay = 10000
            self.spawn()

    def spawn(self):
        if self.spawnCounter == 0:
            for i in range(0, 5):
                self.player.addEnemy(cc.SpawnRandomEnemy(5, (255, 0, 0), self.player, 200))
        elif self.spawnCounter == 1:
            for i in range(0, 3):
                self.player.addEnemy(cc.SpawnRandomEnemy(5, (255, 0, 0), self.player, 200))
        elif self.spawnCounter == 2:
            self.player.addEnemy(cc.SpawnChaserEnemy(5, (0, 255, 0), self.player, True))
        elif self.spawnCounter == 3:
            self.player.addEnemy(cc.SpawnChaserEnemy(5, (0, 0, 255), self.player, False))
        elif self.spawnCounter == 4:
            for i in range(0, 3):
                self.player.addEnemy(cc.SpawnRandomEnemy(4, (100, 100, 100), self.player, 100))
        elif self.spawnCounter == 5:
            for i in range(0, 3):
                self.player.addEnemy(cc.SpawnRandomEnemy(4, (100, 100, 100), self.player, 100))
            # stop spawning
            self.finishedSpawning = True
        self.spawnCounter += 1