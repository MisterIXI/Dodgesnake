
import pygame
import random
import math

# Directions:
# 0 = Up
# 1 = Up-Right
# 2 = Right
# 3 = Down-Right
# 4 = Down
# 5 = Down-Left
# 6 = Left
# 7 = Up-Left

class Enemy:
    def __init__(self, startPos, size, moveDelay, color, player):
        self.pos = startPos
        self.size = size
        self.moveDelay = moveDelay
        self.color = color
        self.player = player
        self.screen = player.screen
        self.direction = random.randint(0, 7)
        self.currentTicks = 0
        print("Enemy created with start direction " + str(self.direction))

    def tick(self, clockTick):
        self.currentTicks += clockTick
        if self.currentTicks >= self.moveDelay:
            self.currentTicks = 0
            isColliding = None
            for enemy in self.player.enemies:
                if(enemy != self):
                    if pygame.Rect.colliderect(pygame.Rect(self.pos.x, self.pos.y, self.size, self.size), pygame.Rect(enemy.pos.x, enemy.pos.y, enemy.size, enemy.size)):
                        isColliding = enemy
                        break
            if isColliding is not None:
                self.onCollision(clockTick, isColliding)
            else:
                self.move(clockTick)
        pygame.draw.rect(self.screen, self.color, (self.pos.x,
                         self.pos.y, self.size, self.size))

    def onCollision(self, clockTick, other):
        # Try to unstuck
        if self.pos.x < other.pos.x:
            if self.pos.x > 0:
                self.pos.x -= 1
        elif self.pos.x > other.pos.x:
            if self.pos.x < self.screen.get_width() - self.size:
                self.pos.x += 1
        if self.pos.y < other.pos.y:
            if self.pos.y > 0:
                self.pos.y -= 1
        elif self.pos.y > other.pos.y:
            if self.pos.y < self.screen.get_height() - self.size:
                self.pos.y += 1
        # raise NotImplementedError("This method must be implemented by a subclass")

    def move(self, clockTick):
        raise NotImplementedError("This method must be implemented by a subclass")


class RandomEnemy(Enemy):
    def __init__(self, startPos, size, speed, color, player, dirChangeDelay):
        super().__init__(startPos, size, speed, color, player)
        self.dirTicks = 0
        self.dirChangeDelay = dirChangeDelay
    
    def onCollision(self, clockTick, isColliding):
        self.direction = (self.direction + 4) % 8
        self.move(clockTick)


    def move(self, clockTick):
        self.dirTicks -= clockTick
        screenHeight = self.screen.get_height()
        screenWidth = self.screen.get_width()
        # Change direction
        if self.dirTicks <= 0:
            self.dirTicks = random.randint(0, self.dirChangeDelay) + 10
            self.direction = random.randint(0, 7)
            # print("New direction: " + str(self.direction))
        # Actual Movement
        if self.direction == 0:
            if self.pos.y > 0:
                self.pos.y -= 1
            else:
                self.direction = 4
        elif self.direction == 1:
            if self.pos.y > 0 and self.pos.x < screenWidth - self.size:
                self.pos.y -= 1
                self.pos.x += 1
            else:
                self.direction = 5
        elif self.direction == 2:
            if self.pos.x < screenWidth - self.size:
                self.pos.x += 1
            else:
                self.direction = 6
        elif self.direction == 3:
            if self.pos.y <screenHeight - self.size and self.pos.x < screenWidth - self.size:
                self.pos.y += 1
                self.pos.x += 1
            else:
                self.direction = 7
        elif self.direction == 4:
            if self.pos.y < screenHeight - self.size:
                self.pos.y += 1
            else:
                self.direction = 0
        elif self.direction == 5:
            if self.pos.y < screenHeight - self.size and self.pos.x > 0:
                self.pos.y += 1
                self.pos.x -= 1
            else:
                self.direction = 1
        elif self.direction == 6:
            if self.pos.x > 0:
                self.pos.x -= 1
            else:
                self.direction = 2
        elif self.direction == 7:
            if self.pos.y > 0 and self.pos.x > 0:
                self.pos.y -= 1
                self.pos.x -= 1
            else:
                self.direction = 3

class ChasingEnemy(Enemy):
    def __init__(self, startPos, size, moveDelay, color, player, isVerticalChaser):
        super().__init__(startPos, size, moveDelay, color, player)
        self.isVerticalChaser = isVerticalChaser

    def tick(self, clockTick):
        return super().tick(clockTick)
    
    
    def chaseUp(self):
        if self.player.pos.y > self.pos.y:
            if self.pos.y < self.screen.get_height() - self.size:
                self.pos.y += 1
                return True
        elif self.player.pos.y < self.pos.y:
            if self.pos.y > 0:
                self.pos.y -= 1
                return True
        return False

    def chaseDown(self):
        if self.player.pos.x > self.pos.x:
            if self.pos.x < self.screen.get_width() - self.size:
                self.pos.x += 1
                return True
        elif self.player.pos.x < self.pos.x:
            if self.pos.x > 0:
                self.pos.x -= 1
                return True
        return False

    def move(self, clockTick):
        if self.isVerticalChaser:
            if not self.chaseUp():
                self.chaseDown()
        else:
            if not self.chaseDown():
                self.chaseUp()
