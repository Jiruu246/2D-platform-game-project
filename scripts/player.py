
from scripts.terrain import BLOCK_SIZE
from scripts.setting import *
from scripts.sprtiesheet import Spritesheet
from scripts.layer import *

PLAYER_SIZE = 96
PLAYER_WIDTH = 50
PLAYER_VEL = 4
DELAY_MOVE = 3
JUMP = 20

class Player:

    def __init__(self):
        self.stand_right = Spritesheet('media/player_1_standby_right.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)
        self.stand_left = Spritesheet('media/player_1_standby_left.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)
        self.walk_right = Spritesheet('media/player_1_run_right.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)
        self.walk_left = Spritesheet('media/player_1_run_left.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)
        self.jump_right = Spritesheet('media/player_1_jump_right.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)
        self.jump_left = Spritesheet('media/player_1_jump_left.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)
        self.fall_right = Spritesheet('media/player_1_fall_right.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)
        self.fall_left = Spritesheet('media/player_1_fall_left.png').load_spritesheet(PLAYER_SIZE, PLAYER_SIZE)

        self.sprite = self.stand_right
        self.rect = self.sprite[0].get_rect()
        self.rect.x = 100
        self.rect.y = 500
        self.maxhealth = 10.0 #set in decimal
        self.health = self.maxhealth

        self.dir = 1

        self.move_x = 0
        self.moving = False
        self.jumping = 0
        self.gravity = 0

    def update(self):

        if self.moving:
            if self.move_x > 0:
                self.move_x -= 1
                self.rect.x += PLAYER_VEL
            elif self.move_x < 0:
                self.move_x += 1
                self.rect.x -= PLAYER_VEL
            elif self.move_x == 0:
                self.moving = False
        else:
            if self.dir == -1:
                self.sprite = self.stand_left
            elif self.dir == 1:
                self.sprite = self.stand_right
        

        
        if self.jumping > 0:
            self.jumping -= 1
            for i in range(self.jumping):
                self.rect.y -= 1
            if self.dir == -1:
                self.sprite = self.jump_left
            elif self.dir == 1:
                self.sprite = self.jump_right 

    
    def move_left(self):
        self.move_x = -DELAY_MOVE
        self.moving = True
        if self.jumping == 0:
            self.sprite = self.walk_left 
  

    def move_right(self):    
        self.move_x = DELAY_MOVE
        self.moving = True
        if self.jumping == 0:
            self.sprite = self.walk_right 
    
    def fall(self):
        if self.jumping == 0:
            if self.gravity == 0:
                self.gravity = 1
            else:
                if self.gravity <= 7:
                    self.gravity += 1
                for i in range(self.gravity):
                    self.rect.y += 1

            if self.dir == -1:
                self.sprite = self.fall_left
            elif self.dir == 1:
                self.sprite = self.fall_right
            

    
    def hit_ground(self):
        self.gravity = 0
        self.rect.bottom = ((ceil((self.rect.bottom + 5)/BLOCK_SIZE) - 1) * BLOCK_SIZE) + 1
    
    def jump(self):
        if self.jumping == 0:
            self.jumping = JUMP     

    def is_jumping(self):
        return self.jumping > 0

    def reset_jump(self):
        self.jumping = 0
    
    def climb_up(self):
        self.rect.y -= 4
    
    def climb_down(self):
        self.rect.y += 4
    
    def draw(self, off_set):
        frame = pygame.time.get_ticks() // 180 % len(self.sprite)
    
        screen.blit(self.sprite[frame], (self.rect.x + off_set[0], self.rect.y + off_set[1]))
        pygame.draw.rect(screen, (255, 255, 255), (self.rect.x + off_set[0], self.rect.y + off_set[1], self.rect.width, self.rect.height), 2)
