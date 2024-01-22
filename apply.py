import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# TODO you must:
# create a recognizable drawing
# use at least 12 'draw' statements
# use at least 3 'draw' functions from pygame
# (circle, line, rectangle, etc)
# use optional parameters at least once

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
