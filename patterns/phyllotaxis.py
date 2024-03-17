import pygame
import math
from sys import exit
import random
pygame.init()

screen = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()
angle = 137.3
angle1 = 137.5
angle2 = 137.6
n = 0
c = 10
while True :

    for event in pygame.event.get() :
        if event.type ==pygame.QUIT :
            pygame.quit()
            exit()
    a = n * math.degrees(angle2)
    r = c * math.sqrt(n)
    x = r * math.cos(a) + 1080/2
    y = r * math.sin(a) + 720/2
    color = (n % 256,100,3)
    pygame.draw.circle(screen,color,(x,y),2)
    n += 1
    pygame.display.update()
    clock.tick(30)



    