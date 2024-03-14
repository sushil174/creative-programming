import pygame
import math
import random
from sys import exit


def random2D() :
    angle = random.uniform(0,2.0*math.pi)
    length = 1
    pos = pygame.math.Vector2(length * math.cos(angle), length * math.sin(angle))
    return pos

class accel :
    def __init__(self,x,y) :
        self.pos = pygame.math.Vector2(x,y)
        self.prev = self.pos

    def update(self) :

        angle = random2D() 
        r = random.randrange(0,100)
        angle = angle * random.randrange(25,100) if r < 178 else pygame.math.Vector2.normalize(angle) * 2
        self.pos = self.pos + angle

    def show(self,surface) :
        c = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        pygame.draw.line(surface,c,self.pos,self.prev)
        self.prev = self.pos

pygame.init()
screen = pygame.display.set_mode((600,600))
display = pygame.Surface((200,200))
clock = pygame.time.Clock()
accel = accel(100,100)
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit()
            pygame.quit

    accel.update()
    accel.show(display)
    screen.blit(pygame.transform.scale(display,screen.get_size()),(0,0))
    pygame.display.update()
    clock.tick(30)