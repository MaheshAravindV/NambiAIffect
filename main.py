import math

import pygame
import sys

pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# BG_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)

background_image = pygame.image.load("bg3.png")
bg_x, bg_y = (0, 0)
rockets = []


class Triangle:
    def __init__(self, base_length, base_middle, direction):
        self.base_middle = base_middle
        self.direction = direction
        self.base_length = base_length
        self.points = self.find_pts()

    def set_direction(self, direction):
        self.direction = direction
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


player = Triangle(20, [300, 300], math.pi/2)


def find_direction():
    mouse = pygame.mouse.get_pos()
    y = 300 - mouse[1]
    x = mouse[0] - 300
    if x == 0:
        if y >= 0:
            return -math.pi/2
        return math.pi/2
    direction = math.atan(y / x)
    if x < 0:
        direction = math.pi + direction
    return direction


def print_bg():
    global bg_x, bg_y
    if bg_x > 600:
        bg_x -= 600
    if bg_x < 0:
        bg_x += 600
    if bg_y > 600:
        bg_y -= 600
    if bg_y < 0:
        bg_y += 600
    for x_off in range(-1, 2):
        for y_off in range(-1, 2):
            screen.blit(background_image, (bg_x + x_off * 600, bg_y + y_off * 600))


while 1:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    print_bg()
    player_direction = find_direction()

    velocity = 10
    bg_x += math.cos(player_direction + math.pi) * velocity
    bg_y -= math.sin(player_direction + math.pi) * velocity

    player.set_direction(player_direction)
    pygame.draw.polygon(screen, WHITE, player.points)
    pygame.display.flip()
