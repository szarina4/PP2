import pygame ,math
import datetime
pygame.init()

display=pygame.display.set_mode((800,800))
clock=pygame.time.Clock()
FPS=50

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def print_text(text,position):
    font=pygame.font.SysFont("Castellar",40,True,False)
    surface=font.render(text,True,BLACK)
    display.blit(surface,position)
def convert_degrees_to_pygame(R,theta):
    y=math.cos(math.pi*theta/180)*R
    x=math.sin(math.pi*theta/180)*R
    return x+400-15,-(y-400)-15

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    display.fill(WHITE)
    pygame.draw.circle(display,BLACK,(400,400),400,4)


    for number in range(1,13):
        print_text(str(number),convert_degrees_to_pygame(350,number*30))

    current_time=datetime.datetime.now()
    seconds=current_time.second
    minutes=current_time.minute
    

    #Minute
    R=400
    theta=(minutes+seconds/60)*(360/60)
    pygame.draw.line(display,BLACK,(400,400),convert_degrees_to_pygame(R,theta),6)

    #Second
    
    R=400
    theta=seconds*(360/60)
    pygame.draw.line(display,BLUE,(400,400),convert_degrees_to_pygame(R,theta),6)

    clock.tick(FPS)
   
    pygame.display.flip()