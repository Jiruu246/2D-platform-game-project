from scripts.layer import Layer
import pygame
from scripts.sprtiesheet import Spritesheet
from scripts.map import Map


pygame.init()

screen_width = 1200
screen_height = 800
screen_area = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_area)

player = Spritesheet('media/area02_level_tiles.png').load_spritesheet(48,48)

run = True
new_map = Map()



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #screen.blit(player[0], (0,0))
    #screen.blit(player[1], (96,0))
    #screen.blit(player[2], (192,0))
    #screen.blit(player[3], (288,0))
    #screen.blit(player[4], (288,0))
    #print(player[0])
    #screen.blit(player, (0,0))
    
    new_map.draw_map()

    pygame.display.update()

pygame.quit()
