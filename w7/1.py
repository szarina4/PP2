import pygame ,math
import datetime
pygame.init()
#Setting the display,fps
display=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
FPS=50

#The backqround
bq=pygame.image.load("mickey.jpg")
bq=pygame.transform.scale(bq,(800,800)) 

#min_arrow=pygame.image.load("left.png")
#min_arrow=pygame.transform.scale(min_arrow,(300,300)) 

#the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


#The position function
def convert_degrees_to_pygame(R,theta):
    y=math.cos(math.pi*theta/180)*R
    x=math.sin(math.pi*theta/180)*R
    return x+400+35,-(y-400)+70

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Setting the bq
    display.blit(bq,(0,0))


    #Getting the time
    current_time=datetime.datetime.now()
    seconds=current_time.second
    minutes=current_time.minute
    

    #Minute
    R=300
    theta=(minutes+seconds/60)*(360/60)
    #display.blit(min_arrow,convert_degrees_to_pygame(R,theta))
    pygame.draw.line(display,BLACK,(400,400),convert_degrees_to_pygame(R,theta),6)

    #Second
    
    R=350
    theta=seconds*(360/60)
    pygame.draw.line(display,BLUE,(400,400),convert_degrees_to_pygame(R,theta),6)

    clock.tick(FPS)
   
    pygame.display.flip()