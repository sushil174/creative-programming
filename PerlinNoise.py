import pygame
from sys import exit
import random
from perlin_noise import PerlinNoise

def map_range(value, start1, stop1, start2, stop2):
   return (value - start1) / (stop1 - start1) * (stop2 - start2) + start2
pygame.init()

screen = pygame.display.set_mode((600,600))
display = pygame.Surface((200,200))
clock = pygame.time.Clock()
noise = PerlinNoise()
xoff = 0
yoff = 0
inc = 0.01
while True:
    display.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    for y in range(0,200):
        xoff = 0
        for x in range(0,200):
            r = noise([xoff,yoff]) * 255
            #r = map_range(noise([xoff,yoff]),0,1,100,255) 
            #r = random.randint(0,255)
            if r < 0: r = r * -1
            pygame.draw.circle(display,(r,r,r,255),(x,y),1)
            xoff += inc
        yoff += inc


    # x = map_range(noise(xoff1),0,1,200,400)
    # y = map_range(noise(xoff2),0,1,200,400)

    # xoff1 += 0.1
    # xoff2 += 0.1
    # #x = random.randint(0,400)
    # pygame.draw.circle(screen,'white',(x,y),14)
    screen.blit(pygame.transform.scale(display,screen.get_size()),(0,0))
    pygame.display.update()
    clock.tick(30)