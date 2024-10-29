import pygame
import math
from sys import exit
import random

pygame.init()

screen = pygame.display.set_mode((1080,720))
clock = pygame.time.Clock()
t = []
pos = (0,0)
circle = []
class circles:
    def __init__(self,pos) :
        self.pos = pos
        self.radius = 20
        self.width = 2
        self.v = 0.1
        self.b = 3
        
    def update(self) :
        self.radius += self.b
        
        self.destroy()

    def destroy(self):
        if self.radius >= 200 : del self


    def show(self,surface) :
        #pygame.draw.circle(surface,'white',self.pos,self.radius,self.width)
        pygame.draw.circle(surface,'white',self.pos,self.radius,self.width)


while True :
    screen.fill('black')
    for event in pygame.event.get() :
        if event.type ==pygame.QUIT :
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            t.append(circles(pos))

    for c in t :
        c.update()
        c.show(screen)
        if c.radius > 100 :
            t.remove(c)
    
    pygame.display.update()
    clock.tick(30)



    