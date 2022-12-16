import pygame
import sys
import random
from block import BLOCK_SIZE
from screen import SH, SW, Screen
from snake import Snake

pygame.init()

FONT = pygame.font.get_default_font()

screen = Screen()
surface = screen.getSurface()
clock = pygame.time.Clock()

screen.drawGrid(surface)

snake = Snake()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    snake.update()

    screen.reset(surface, 'black')

    snake.drawSnake(surface)   

    pygame.display.update()
    clock.tick(10)