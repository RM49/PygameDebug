import pygame
import PygameDebug
import time
import random

run = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))

# initialise debug, pass screen, colour, fontsize
debug = PygameDebug.Debug(screen, (0, 255, 0), 16)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    screen.fill((0,0,0))
    
    # placeholder variables, can be changed and will be updated
    x = 1
    y = 2
    z = "not used yet"
    
    # update and format as seen
    debug.Update(("X", x), ("Y", y), ("Z", z))
    
    pygame.display.flip()
    
pygame.quit()
