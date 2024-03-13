import pygame
from sys import exit
import random
import math

def random2D() :
    angle = random.uniform(0,2.0*math.pi)
    length = 1
    pos = pygame.math.Vector2(length * math.cos(angle), length * math.sin(angle))
    return pos
    
screen = pygame.display.set_mode((600,600))
#display = pygame.Surface((200,200))
clock = pygame.time.Clock()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    v = pygame.math.Vector2(300,300)
    mouse = pygame.math.Vector2(pygame.mouse.get_pos())
    pos = mouse - v
    

    # pos = random2D() * random.randint(10,50)
    # pos.x = pos.x + 100
    # pos.y = pos.y + 100
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),50)
    pygame.draw.line(screen,color,(300,300),pygame.mouse.get_pos(),5)
    


    pygame.display.update()
    #screen.blit(pygame.transform.scale(display,screen.get_size()),(0,0))
    clock.tick(30)
