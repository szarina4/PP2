import pygame,math
#DRawing the rectangle
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW=(255, 255, 0)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
screen.fill(WHITE)
game_over = False
equ_tr=pygame.image.load("equ.png").convert_alpha()
equ_tr=pygame.transform.scale(equ_tr,(40,40)) 
equ_rect=equ_tr.get_rect()
rhomb_im=pygame.image.load("Rhomb.png").convert_alpha()
rhomb_im=pygame.transform.scale(rhomb_im,(60,60)) 
rhomb_rect=rhomb_im.get_rect()

prev, cur = None, None
color=GREEN
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    
    
    pressed = pygame.key.get_pressed()
    #Drawing a rectangle  r-rectangle
    if pressed[pygame.K_r]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if prev and cur:
                my_rect=pygame.Rect((prev[0],prev[1],abs(cur[0]-prev[0]),abs(cur[1]-prev[1])))
                pygame.draw.rect(screen,color,my_rect)
    #c-circle just drag    
    if pressed[pygame.K_c]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if prev and cur:
                rad=math.sqrt(math.pow(prev[0]-cur[0],2)+math.pow(prev[1]-cur[1],2))
                pygame.draw.circle(screen,color,(prev[0],prev[1]),rad)
    #The eraser cur =20
    if pressed[pygame.K_e]:
      if event.type == pygame.MOUSEMOTION:
          cur = pygame.mouse.get_pos()
          pygame.draw.circle(screen,WHITE,(cur[0],cur[1]),20)
    #The color change
    if pressed[pygame.K_1] or  pressed[pygame.K_KP_1]:     
      color=RED
    if pressed[pygame.K_2] or  pressed[pygame.K_KP_2]:     
      color=GREEN
    if pressed[pygame.K_3] or  pressed[pygame.K_KP_3]:     
      color=BLUE
    if pressed[pygame.K_4] or  pressed[pygame.K_KP_4]:     
      color=BLACK
    if pressed[pygame.K_5] or  pressed[pygame.K_KP_5]:     
      color=YELLOW
    
  #The square
  if pressed[pygame.K_s]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if prev and cur:
                my_rect=pygame.Rect((prev[0],prev[1],abs(cur[0]-prev[0]),abs(cur[0]-prev[0])))
                pygame.draw.rect(screen,color,my_rect)
  #right triangle
  if pressed[pygame.K_q]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if prev and cur:
               pygame.draw.polygon(screen, color, [(prev[0],prev[1]), (prev[0],cur[1]), (cur[0],cur[1])])
  #equilateral triangle t
  if pressed[pygame.K_t]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            if prev:
                  equ_rect.center=prev
                  screen.blit(equ_tr,equ_rect)
  #rhomb -h 
  if pressed[pygame.K_h]:
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            if prev:
                  rhomb_rect.center=prev
                  screen.blit(rhomb_im,rhomb_rect)
             
          


          
  pygame.display.update()

  clock.tick(60)