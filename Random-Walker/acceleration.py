import pygame
from sys import exit
import random
import math

def random2D() :
    angle = random.uniform(0,2.0*math.pi)
    length = 1
    pos = pygame.math.Vector2(length * math.cos(angle), length * math.sin(angle))
    return pos    

def magSq(v) :
    return (v.x*v.x + v.y*v.y)  

def limit(v,max) :
    if magSq(v) > max*max :
     v = pygame.math.Vector2.normalize(v) * max


class accel :
    def __init__(self,x,y):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = random2D() 
        self.vel = self.vel * random.randint(1,5)
        self.acc = pygame.math.Vector2()
        self.max = 5

    def update(self):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        self.acc = mouse - self.pos
        self.acc = pygame.math.Vector2.normalize(self.acc) * 1
        self.vel = self.vel + self.acc
        
        
        if magSq(self.vel) > self.max*self.max:
            self.vel = pygame.math.Vector2.normalize(self.vel) * self.max
        
        self.pos = self.pos + self.vel

    
    def show(self,surface):
        pygame.draw.circle(surface,'white',self.pos,20,1)



screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
accel = accel(300,300)
while True :
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    accel.update()
    accel.show(screen)
    pygame.display.update()
    clock.tick(30)
