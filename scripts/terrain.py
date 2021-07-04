import pygame
from scripts.sprtiesheet import Spritesheet

BLOCK_SIZE = 48

tiles_name = {
    'Air' : 0,
    'Up_left_dirt' : 1,
    'Grass' : 2,
    'Groud_Grass' : 3,
    'Float_grass' : 4,
    'Wood' : 5,
    'Second_level_grass' : 6,
    'Inner_Grass' : 9,
    'Left_side_grass_with_flower' : 11,
    'Hardblock1' : 12,
    'Left_side_grass' : 13,
    'Hardblock2' : 14,
    'Left_face_dirt' : 15,
    'Hardblock3' : 16,
    'Down_left_dirt' : 17,
    'Hardblock4' : 18,
    'Dirt_with_rock' : 19,
    'Up_right_dirt' : 20,
    'Single_hard_block' : 21,
    'Right_face_dirt' : 22,
    'Down_right_dirt' : 23,
    'Dirt_with_rock2' : 24,
    'Skull1' : 25,
    'Top_left_rock' : 26,
    'Skull2' : 27,
    'Top_right_rock' : 28,
    'Skull3' : 29,
    'Right_side_grass_with_flower' : 31,
    'Grass_with_leaf' : 32,
    'Blank_dirt' : 33,
    'Lader' : 34,
    'Grass_with_small_leaf' : 35,
    'Top_right_grass' : 36,
    'Top_left_grass' : 37,
    'Bottom_grass' : 38,
    'Bottom_left_grass' : 39,
    'Bottom_right_grass' : 40,
    'Left_side_wall' : 41,
    'Sign' : 42,
    'Small_tree' : 43,
    'Skull4' : 44,
    'SurfGrass2' : 45,
}

class Terrain():
    def __init__(self):
        self.tile_set = Spritesheet('media/area02_level_tiles.png').load_spritesheet(BLOCK_SIZE, BLOCK_SIZE)