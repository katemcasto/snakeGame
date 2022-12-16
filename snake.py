import pygame
from block import BLOCK_SIZE

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xDirection = 1
        self.yDirection = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xDirection * BLOCK_SIZE
        self.head.y += self.yDirection * BLOCK_SIZE
        self.body.remove(self.head)

    def drawSnake(snake, surface):
        pygame.draw.rect(surface, "green", snake.head)
        for square in snake.body:
            pygame.draw.rect(surface, "green", square) 