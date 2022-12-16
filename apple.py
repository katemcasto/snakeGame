import random
import pygame
from screen import SW, SH
from block import BLOCK_SIZE

class Apple:
    def __init__(self):
        self.x = random.randint(0, SW)
        self.y = random.randint(0, SH)
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        
    def update(self, surface):
        pygame.draw.rect(surface, "red", self.rect)