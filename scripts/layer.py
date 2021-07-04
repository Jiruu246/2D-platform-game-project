import pygame

screen_width = 1200
screen_height = 800
screen_area = (screen_width, screen_height)

pygame.display.set_caption("Guns Arena")
screen = pygame.display.set_mode(screen_area)

class Layer():
    
    background_layer = pygame.surface.Surface(screen_area)
    map_layer = pygame.surface.Surface(screen_area)
    player_layer = pygame.surface.Surface(screen_area)
    ui_layer = pygame.surface.Surface(screen_area)