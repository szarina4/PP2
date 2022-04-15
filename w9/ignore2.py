from types import CellType
import pygame,random
pygame.init()

#Setting the display and block cells
cell_size=30
cell_num=22
screen=pygame.display.set_mode((cell_size*cell_num,cell_size*cell_num))

#FPS
clock=pygame.time.Clock()
FPS=60

running=True

red_apple=pygame.image.load("redapple.png").convert_alpha()
red_apple=pygame.transform.scale(red_apple,(30,30)) 
my_font=pygame.font.Font(None,30)
#The food class
class FOOD:
    #Randomizing its places
    def __init__(self):
        self.randomize()
        self.crunch=pygame.mixer.Sound("crunch.mp3")
    #Drawing the food
    def draw(self):
        thefood=pygame.Rect(self.x*cell_size,self.y*cell_size,cell_size,cell_size)
        screen.blit(red_apple,thefood)
    #Making sure it is in random places after being eaten
    def randomize(self):
        self.x=random.randint(0,cell_num-1)
        self.y=random.randint(0,cell_num-1)
    
    def sound(self):
        self.crunch.play()
        
#The snake class
class SNAKE:
    
    def __init__(self):
        self.body=[[7,17],[6,17],[5,17]]
        self.dx=1
        self.dy=0
        self.new_block=False
    
    def draw(self):
        #the head
        head=(self.body[0][0]*cell_size,self.body[0][1]*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(0,0,0),head)
        #the rest
        for i in range(1,len(self.body)):
            x_pos,y_pos=self.body[i][0],self.body[i][1]
            blocks=(x_pos*cell_size,y_pos*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(255, 240, 77),blocks)
       
    def move(self): 
        if self.new_block:
            body_copy=self.body[:]
            body_copy.insert(0,[body_copy[0][0]+self.dx,body_copy[0][1]+self.dy])
            self.body=body_copy
            self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,[body_copy[0][0]+self.dx,body_copy[0][1]+self.dy])
            self.body=body_copy
       
    def add_block(self):
        self.new_block=True
        self.move()
        
class MAIN():
    def __init__(self):
        self.snake=SNAKE()
        self.food=FOOD()
        self.wall=WALL()
    def food_was_eaten(self):
        if self.food.x==self.snake.body[0][0] and self.food.y==self.snake.body[0][1]:
            self.food.sound()
            self.food.randomize()
            self.snake.add_block()

    def update(self):
        self.snake.move()
        self.food_was_eaten()
        self.check_fail()
    def draw_objects(self):
        self.wall.put_thewalls()
        self.wall.draw()
        self.food.draw()
        self.snake.draw()
        self.score()
    def check_fail(self):
        #If snake hits itself 
        for i in self.snake.body[1:]:
            if i[0]==self.snake.body[0][0] and i[1]==self.snake.body[0][1]:
                self.game_over()
        #If it hits the border
        if not 0<=self.snake.body[0][0]<cell_num or not 0<=self.snake.body[0][1]<cell_num:
            self.game_over()
        #If it hits to the wall
        for i in self.wall.body[:]:
            if i[0]==self.snake.body[0][0] and i[1]==self.snake.body[0][1]:
                self.game_over()

    def score(self):
        score=len(self.snake.body)-3
        score_surface=my_font.render(str(score),True,(255,255,255))
        screen.blit(score_surface,(10,10))
    

    """def wall_food_collision(self):
        while 1:
             for i in range(0,len(self.wall.body)):
                if self.food.x!="""

    def game_over(self):
        global running
        running=False
 
class WALL():
    def __init__(self):
        self.body=[]
        self.level=1

    def put_thewalls(self):
        with open("level"+str(self.level)+".txt","r") as f:
            data=f.readlines()
            for i, line in enumerate(data):
                for j, value in enumerate(line):
                    if value == '#':
                     self.body.append([j, i])

    def draw(self):
        for i in range(0,len(self.body)):
            x_pos,y_pos=self.body[i][0],self.body[i][1]
            walls=(x_pos*cell_size,y_pos*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(178, 102,255),walls)
  
    #Game collison with walls done
    #foos score done
    # Add levels and move on after certain food score
    # Add everything of wall to game to simplify
    #FOod timer 
    # The food doesnt spawn on walls 
            



game=MAIN()

#So it doesnt move instantly
snake_timer=pygame.USEREVENT
pygame.time.set_timer(snake_timer, 150)
#The main loop
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #making sure it doesnt inverse itself
                if game.snake.dx!=-1:
                    game.snake.dx,game.snake.dy = 1,0
            if event.key == pygame.K_LEFT:
                if game.snake.dx!=1:
                    game.snake.dx,game.snake.dy = -1,0
            if event.key == pygame.K_UP:
                if game.snake.dy!=1:
                    game.snake.dx,game.snake.dy = 0,-1
            if event.key == pygame.K_DOWN:
                if game.snake.dy!=-1:
                    game.snake.dx,game.snake.dy = 0,1
        if event.type==snake_timer:
            game.update()
    
    screen.fill((119,221,119))
    game.draw_objects()
    
    pygame.display.update()
    clock.tick(FPS)


#Problem is smoothenss