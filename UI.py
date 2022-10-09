import pygame
import Spawner

class GameOverlay():
    def __init__(self, spawner, screen):
        self.font = pygame.font.SysFont("monospace", 30)
        self.score = 0
        self.scoreLabel = self.font.render("Score: " + str((int)(self.score/100)), 1, (255, 255, 255))
        self.Spawner = spawner
        self.spawnCountdown = self.font.render("Next wave in: " + str((int)(self.Spawner.spawnDelay/1000)), 1, (255, 255, 255))
        self.screen = screen
    
    def reset(self):
        self.score = 0

    def tick(self, clockTick):
        self.score += clockTick
        self.scoreLabel = self.font.render("Score: " + str((int)(self.score/100)), 1, (255, 255, 255))
        if self.Spawner.finishedSpawning:
            self.spawnCountdown = self.font.render("No more waves... Survive!", 1, (255, 255, 255))
        else:
            self.spawnCountdown = self.font.render("Next wave in: " + str((int)(self.Spawner.spawnDelay/1000)), 1, (255, 255, 255))
        self.screen.blit(self.scoreLabel, (10, 5))
        self.screen.blit(self.spawnCountdown, (10, 30))