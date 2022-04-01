import pygame
from datetime import datetime
import math
pygame.init()

#Getting the curr time
thedate=datetime.now()
seconds=thedate.second
minutes=thedate.minute

#Making the screen
screen = pygame.display.set_mode((600, 600))
running = True
#FPS
clock = pygame.time.Clock()
FPS = 60

mickey=pygame.image.load('mickey.jpg')
mickey = pygame.transform.scale(mickey,(600,600))


sec_arrow=pygame.image.load('right.jpg')

while running:

    screen.blit(mickey,(0,0))
    screen.blit(sec_arrow,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                    
    
    pygame.display.flip()
    clock.tick(FPS)
