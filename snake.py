import pygame
from block import BLOCK_SIZE

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xDirection = 1
        self.yDirection = 0
        self.head = [pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

