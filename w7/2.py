import pygame
pygame.init()

#playing the first song
_songs=["song1.mp3","song2.mp3","song3.mp3","song4.mp3","song5.mp3"]
pygame.mixer.music.load('C:\\Users\\bolat\\Documents\\PP2\\PP2\\w7\\'+_songs[0])
pygame.mixer.music.play()


# Creating main window
screen = pygame.display.set_mode((500, 500))
running = True


# RGB - Red Green Blue [0-255]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)




# Main loop
while running:
    
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #Checking if music is playing
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key ==pygame.K_RIGHT:
                _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
                pygame.mixer.music.load('C:\\Users\\bolat\\Documents\\PP2\\PP2\\w7\\'+_songs[0])
                pygame.mixer.music.play(0)
                
                
            if event.key ==pygame.K_LEFT:
                _songs = [_songs[-1]] + _songs[:4] # move current song to the back of the list and making sure that the song on first place is the prev song
                pygame.mixer.music.load('C:\\Users\\bolat\\Documents\\PP2\\PP2\\w7\\'+_songs[0])
                pygame.mixer.music.play(0)

                    
    
    screen.fill(WHITE)

    # Screen updating
    pygame.display.flip()