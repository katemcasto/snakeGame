import random
import pygame
from screen import SW, SH
from block import BLOCK_SIZE

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SW)/BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        
    def update(self, surface):
        pygame.draw.rect(surface, "red", self.rect)