import pygame
import sys
import random
from block import BLOCK_SIZE
from screen import SH, SW, Screen
from snake import Snake

pygame.init()

FONT = pygame.font.get_default_font()

surface = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, "#3c3c3b", rect, 1)

drawGrid()

snake = Snake()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(surface, "green", snake.head[0])
    for square in snake.body:
        pygame.draw.rect(surface, "green", square)      

    pygame.display.update()
    clock.tick(10)