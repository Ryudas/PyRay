import pygame as pg  
import numpy as np
import random


HEIGHT = 320
WIDTH = 480
# set the size of the screen as multiples of the array
cellsize = 1
SCREEN_HEIGHT = HEIGHT * cellsize 
SCREEN_WIDTH = WIDTH * cellsize

# create a 3D array with 600x600x3 (the last dimension is for the RGB color)
pixel_array = np.ndarray((HEIGHT, WIDTH, 3)) 

# color dictionary, represents white, red and blue
color_dict = {
        0: (255, 255, 255), 
        1: (255, 0, 0),
        2: (0, 0, 255)
        }

# pick a random color tuple from the color dict
for i in range(HEIGHT):
    for j in range(WIDTH):
        pixel_array[i][j] = color_dict[random.randrange(3)]



# Initialize pygame
pg.init()

# Initialize the screen for display
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Clock for limiting framerate of window
clock = pg.time.Clock()


# Create a surface with the size as the array 
surf = pg.Surface((WIDTH, HEIGHT))

 # draw the array onto the surface 
pg.surfarray.blit_array(surf, pixel_array)
# transform the surface to screen size
surf = pg.transform.scale(surf, (WIDTH, HEIGHT)) 

# game loop
running, i = True, -1
print(pixel_array.shape[0] ) 
print(pixel_array.shape[1] )
 
while running: 
    #clock.tick(3000)
    if(i < HEIGHT-1):
        i +=1
    else:
        i =0 
    print(i) 
 

    for event in pg.event.get():  
        if event.type == pg.QUIT:
            running = False

    # for all         
    for k in range(pixel_array.shape[0]):
        pixel_array[k][i] = color_dict[random.randrange(3)]

    # update screen with pixel array        
    pg.surfarray.blit_array(surf, pixel_array)    
    screen.fill((0, 0, 0))

    # blit the transformed surface onto the screen
     # draw the array onto the surface 

    screen.blit(surf, (0, 0)) 

    pg.display.update() 

pg.quit()