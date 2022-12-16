import pygame

from block import BLOCK_SIZE

SW, SH = 800, 800

class Screen:
    def getSurface(self):
        pygame.display.set_caption("Snake!")
        return pygame.display.set_mode((800, 800))

    def drawGrid(self, surface):
        for x in range(0, SW, BLOCK_SIZE):
            for y in range(0, SH, BLOCK_SIZE):
                rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(surface, "#3c3c3b", rect, 1)

    def reset(self, surface, color):
        surface.fill(color)
        self.drawGrid(surface)