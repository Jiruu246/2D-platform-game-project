import pygame
from pygame import image
from scripts.terrain import *
from scripts.layer import *
from scripts.enemy import Enemy

class Map:
    def __init__(self):
        self.terrain = Terrain()
        self.enemies = []
        self.generate_map('levels/level_1.txt')

    def generate_map(self, map_file):
        file = open(map_file, 'r')
        self.lines = file.readlines()
        self.height = len(self.lines)
        self.width = len(self.lines[0]) - 1 # minus 1 for the next line char

        self.tiles = [None] * self.width
        for x in range(self.width):
            self.tiles[x] = [None] * self.height
            for y in range(self.height):
                self.tiles[x][y] = [None] * 3 # 0 index = name, 1 index = img , 2 index = rect
                self.tiles[x][y][0] = tile = self.get_data(self.lines[y][x], x, y)
                if tile != 'Air' and tile != None:
                    i = tiles_name[tile]
                    img = self.terrain.tile_set[i]
                    self.tiles[x][y][1] = img
                    image_rect = img.get_rect()
                    image_rect.x = x * BLOCK_SIZE
                    image_rect.y = y * BLOCK_SIZE
                    self.tiles[x][y][2] = image_rect


    def get_data(self,coor, x, y):
        tiles_set = {
            '$': 'Grass',
            '#': 'Inner_Grass',
            '_': 'Groud_Grass',
            '0': 'Air',
            '+': 'Lader',
            '.': 'Grass_with_leaf',
            ',': 'Grass_with_small_leaf',
            '%': 'Second_level_grass',
            '&': 'Top_right_grass',
            '=': 'Top_left_grass',
            '[': 'Left_side_grass_with_flower',
            ']': 'Right_side_grass_with_flower',
            '-': 'Bottom_grass',
            '{': 'Bottom_left_grass',
            '}': 'Bottom_right_grass',
            '|': 'Left_side_grass',
            '/': 'Left_side_wall',
            '*': 'Single_hard_block',
            '?': 'Sign',
            '~': 'Small_tree',
            '1': 'Skull1',
            '2': 'Skull2',
            '3': 'Skull3',
            '4': 'Skull4',
            'a': 'Hardblock1',
            'b': 'Hardblock2',
            'c': 'Hardblock3',
            'd': 'Hardblock4',
            '!': 'SurfGrass2',
            'e': 'Float_grass',
            'f': 'Blank_dirt',
            'g': 'Up_left_dirt',
            'k': 'Up_right_dirt',
            'l': 'Down_left_dirt',
            'm': 'Down_right_dirt',
            'n': 'Left_face_dirt',
            'o': 'Right_face_dirt',
            'p': 'Dirt_with_rock',
            'q': 'Top_left_rock',
            'r': 'Top_right_rock',
            's': 'Dirt_with_rock2',
            't': 'Wood',
        }

        if coor == 'x':
            self.create_enemy(x, y)

        return tiles_set.get(coor, 'Air')
    
    def create_enemy(self, x, y):
        enemy = Enemy(x * BLOCK_SIZE, y * BLOCK_SIZE)
        self.enemies.append(enemy)
        return 'Air'

    def draw_map(self, off_set):
        for x in range(self.width):
            for y in range(self.height):
                tile = self.tiles[x][y]
                if tile[0] != 'Air':
                    screen.blit(tile[1], (tile[2].x + off_set[0], tile[2].y + off_set[1]))
                    #pygame.draw.rect(screen, (255,255,255), tile[2], 1)

        for enemy in self.enemies:
            enemy.draw(off_set)
            