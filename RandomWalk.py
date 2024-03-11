import pygame
from sys import exit
import random

screen = pygame.display.set_mode((400,400))
display = pygame.Surface((200,200))
clock = pygame.time.Clock()
x = 100
y = 100
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.circle(display,'white',(x,y),1)
    r = random.randint(0,3)
    if r == 0: x += 1
    elif r == 1 : x -= 1
    elif r == 2 : y += 1
    elif r == 3 : y -= 1 

    pygame.display.update()
    screen.blit(pygame.transform.scale(display,screen.get_size()),(0,0))
    clock.tick(30)
