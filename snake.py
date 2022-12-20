import pygame
from apple import Apple
from block import BLOCK_SIZE
from screen import SH, SW

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xDirection = 1
        self.yDirection = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        died = False
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH):
                self.dead = True
        
        if self.dead:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
            self.xDirection = 1
            self.yDirection = 0
            self.dead = False
            died = True

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xDirection * BLOCK_SIZE
        self.head.y += self.yDirection * BLOCK_SIZE
        self.body.remove(self.head)
        return died

    def drawSnake(self, surface):
        pygame.draw.rect(surface, "green", self.head)
        for square in self.body:
            pygame.draw.rect(surface, "green", square) 