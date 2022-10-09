import pygame


class Character:
    def __init__(self, startPos, size, moveDelay, color, screen):
        self.pos = startPos
        self.size = size
        self.moveDelay = moveDelay
        self.color = color
        self.screen = screen
        self.currentTicks = 0
        self.enemies = []

    def tick(self, clockTick):  # returns False on game over
        # Player
        self.currentTicks += clockTick
        if self.currentTicks >= self.moveDelay:
            self.currentTicks = 0
            self.move(clockTick, self.screen)
        if self.checkForGameOver():
            pygame.draw.rect(self.screen, (255, 200, 200),
                             (self.pos.x, self.pos.y, self.size, self.size))
            return False
        pygame.draw.rect(self.screen, self.color,
                         (self.pos.x, self.pos.y, self.size, self.size))
        return True

    def addEnemy(self, enemy):
        self.enemies.append(enemy)

    def checkForGameOver(self):
        for enemy in self.enemies:
            if pygame.Rect.colliderect(pygame.Rect(self.pos.x, self.pos.y, self.size, self.size), pygame.Rect(enemy.pos.x, enemy.pos.y, enemy.size, enemy.size)):
                return True
        return False

    def move(self, clockTick, screen):
        # Check for keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.pos.x > 0:
                self.pos.x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.pos.x < screen.get_width() - self.size:
                self.pos.x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.pos.y > 0:
                self.pos.y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.pos.y < screen.get_height() - self.size:
                self.pos.y += 1
