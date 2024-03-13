import pygame
from sys import exit
import random


class randomwalk :
    def __init__(self,x,y):
        self.pos = pygame.math.Vector2(x,y)
        self.vel = pygame.math.Vector2(1,-1)


    def update(self):
        # self.pos.x = self.pos.x + random.choice([-1,1])
        # self.pos.y = self.pos.y + random.choice([-1,1])
        self.pos = self.pos + self.vel
                                                                                            
    def show(self,surface):
        pygame.draw.circle(surface,'white',(self.pos.x,self.pos.y),1)

screen = pygame.display.set_mode((400,400))
display = pygame.Surface((200,200))
clock = pygame.time.Clock()
walker = randomwalk(100,100)
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    walker.update()
    walker.show(display)
    pygame.display.update()
    screen.blit(pygame.transform.scale(display,screen.get_size()),(0,0))
    clock.tick(30)
