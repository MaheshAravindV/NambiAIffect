import pygame
import sys

pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)

BG_BLUE = (135, 206, 250)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BG_BLUE)
    pygame.display.flip()
