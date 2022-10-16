import math

import pygame
import sys

pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

BG_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)


class Triangle:
    def __init__(self, base_length, base_middle, direction):
        self.base_middle = base_middle
        self.direction = direction
        self.base_length = base_length
        self.points = self.find_pts()

    def find_pts(self):
        cos_theta = math.cos(self.direction)
        sin_theta = math.sin(self.direction)

        x1 = self.base_middle[0] + 2 * self.base_length * cos_theta
        y1 = self.base_middle[1] - 2 * self.base_length * sin_theta

        x2 = self.base_middle[0] + 1/2 * self.base_length * sin_theta
        y2 = self.base_middle[1] + 1/2 * self.base_length * cos_theta

        x3 = self.base_middle[0] - 1/2 * self.base_length * sin_theta
        y3 = self.base_middle[1] - 1/2 * self.base_length * cos_theta

        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (x3, y3)

        return [p1, p2, p3]


player = Triangle(20, (300, 300), math.pi/4);

while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(BG_BLUE)

    pygame.draw.polygon(screen, WHITE, player.points)
    pygame.display.flip()
