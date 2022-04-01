import pygame

# Initialize all configs
pygame.init()

# Creating main window (Surface)
screen = pygame.display.set_mode((500, 500))  # Surface
running = True

# RGB - Red Green Blue [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
# Frame per second
FPS = 60


color = BLUE

x = 25
y = 25

# Main loop
while running:
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x = x + 20
            if event.key == pygame.K_DOWN:
                y = y + 20
            if event.key == pygame.K_UP:
                y = y - 20
            if event.key == pygame.K_LEFT:
                x = x - 20     

    # Getting all pressed buttons
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        y -= 5
    if pressed[pygame.K_DOWN]:
        y += 5
    if pressed[pygame.K_LEFT]:
        x -= 5
    if pressed[pygame.K_RIGHT]:
        x += 5
    #Making sure it doesnt leave the screen   
    if x + 25 >= 500:
        x = 475
    if x-25<0:
        x=25
    if y + 25 >= 500:
        y = 475
    if y-25<0:
        y=25
    
    """ if x + 50 >= 500:
        x = 0
    if x<0:
        x=450
    if y + 50 >= 500:
            y = 0
    if y<0:
        y=450"""
    # Refresh the screen
    screen.fill(WHITE)

    # Drawing the objects
    pygame.draw.circle(screen, color, (x, y), 25)

    # Screen updating
    pygame.display.flip()

    clock.tick(FPS)