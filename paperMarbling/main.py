import pygame
import math
from sys import exit
import random
CIRCLE_DETAIL =30


def map_range(value, start1, stop1, start2, stop2):
   return (value - start1) / (stop1 - start1) * (stop2 - start2) + start2


class Ink : 
    def __init__(self,pos,r):
        self.pos = pygame.math.Vector2(pos)
        self.r = r
        
        self.vertices = []

        for i in range(CIRCLE_DETAIL):
            angle = map_range(i,0,CIRCLE_DETAIL,0,math.pi * 2)
            v = pygame.math.Vector2(math.cos(angle),math.sin(angle))
            v *= self.r
            v += self.pos
            self.vertices.append(v)
            
    def marble(self,other) :
        for v in self.vertices :
            c = other.pos
            r = other.r
            p = v
            p -= c
            m = pygame.math.Vector2.magnitude_squared(p)
            root = math.sqrt(1 + (r*r)/m)
            p *= root
            p += c
            v = p

    def draw(self,surface):
        #c = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        for i in range(len(self.vertices)-1) :
            pygame.draw.line(surface,'white',self.vertices[i],self.vertices[i+1])
        #pygame.draw.circle(surface,'black',self.pos,self.r*2)
        index = len(self.vertices)-1
        pygame.draw.line(surface,'white',self.vertices[0],self.vertices[index])

pygame.init()
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
drop = []


while True :
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            inkDrop = Ink(pos,50)
            for other in drop :
                other.marble(inkDrop)
            drop.append(inkDrop)


    for ink in drop :
        ink.draw(screen)
    pygame.display.update()
    clock.tick(1)


