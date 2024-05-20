import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# a line
x1 = 50
y1 = 50
x2 = 100
y2 = 100
pygame.draw.line(screen, (255,0,0), (x1, y1), (x2, y2))
pygame.display.update()
pygame.time.delay(500)


# a box
x1 = 200
y1 = 100
width = 100
height = 50
pygame.draw.rect(screen, (0,255,0), (x1, y1, width, height))
pygame.display.update()
pygame.time.delay(500)

# a circle
x = 100
y = 200
rad = 20
pygame.draw.circle(screen, (0,0,255), (x, y), rad)
pygame.display.update()


x = 150
y = 150
rad = 20
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # a circle that moves: draw, delay, erase, move
    # FYI we'll learn a better animation technique soon
    pygame.draw.circle(screen, (255,0,255), (x, y), rad)
    pygame.display.update()
    pygame.time.delay(100)
    pygame.draw.circle(screen, (255,255,255), (x,y), rad)
    x += 1
    y += 1
