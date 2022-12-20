import pygame
import sys
import random
from apple import Apple
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

apple = Apple()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.yDirection = 1
                snake.xDirection = 0
            elif event.key == pygame.K_UP:
                snake.yDirection = -1
                snake.xDirection = 0
            elif event.key == pygame.K_RIGHT:
                snake.yDirection = 0
                snake.xDirection = 1
            elif event.key == pygame.K_LEFT:
                snake.yDirection = 0
                snake.xDirection = -1              
    
    if snake.update():
        apple = Apple()

    screen.reset(surface, 'black')

    apple.update(surface)

    pygame.draw.rect(surface, "green", snake.head)
    for square in snake.body:
        pygame.draw.rect(surface, "green", square) 

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y, BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()

    pygame.display.update()
    clock.tick(10)