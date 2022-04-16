from itertools import count
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
cnt_coins=0
z=0 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


coin_sound=pygame.mixer.Sound("coin.mp3")
#Getting the coin image
goldcoin_image=pygame.image.load("gold_coin.png").convert_alpha()
goldcoin_image=pygame.transform.scale(goldcoin_image,(50,40)) 
silvercoin_image=pygame.image.load("silver_coin.png").convert_alpha()
silvercoin_image=pygame.transform.scale(silvercoin_image,(50,40)) 
bronzecoin_image=pygame.image.load("bronze_coin.png").convert_alpha()
bronzecoin_image=pygame.transform.scale(bronzecoin_image,(50,40)) 
#The coin class
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.randomize()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0,400), random.randint(470,570))
    #Random coins with different weights 
    def randomize(self):
        global z
        z=random.randint(1,3)
        if z==1:
            self.image=goldcoin_image
        if z==2:
            self.image=silvercoin_image
        if z==3:
            self.image=bronzecoin_image
        

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
      #moving the enemy car
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE+=1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()





#Creating Sprites Groups
thecoins=pygame.sprite.GroupSingle()


enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

R_COIN=pygame.USEREVENT+1
pygame.time.set_timer(R_COIN, 3000)
 
increment=True
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type==R_COIN:
            C1=Coins()
            thecoins.add(C1)        
    #Showing the money count
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Cars you didnt hit:"+str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    counterofcoins=font_small.render("Score of coins:"+str(cnt_coins),True,BLUE)
    DISPLAYSURF.blit(counterofcoins, (10,30))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    #Adding the coins
    for coin in thecoins:
        DISPLAYSURF.blit(coin.image, coin.rect)

    if pygame.sprite.spritecollideany(P1, thecoins):
          coin_sound.play()
          #checking which type of coin it is 
          if z==1:
                cnt_coins+= 5
          if z==2:
                cnt_coins+= 2
          if z==3:
                cnt_coins+= 1       
          pygame.display.update()
          for coin in thecoins:
            coin.kill()       
    
    #Increasing speed after N coins N=20:
    if cnt_coins>=20 and increment:
        SPEED+=2
        increment=False

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)