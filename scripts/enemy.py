from scripts.sprtiesheet import Spritesheet
from scripts.setting import *
from scripts.layer import *
import random
from scripts.terrain import BLOCK_SIZE


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = 96 # image size
        self.width = 50 # the hitbox width  
        self.height = 96 # the hitbox height
        self.health = 5
        self.speed = 2
        self.vision = 500
        self.attack_range = 500
        self.attack_speed = 1
        self.reload_time = 30

        self.enemy_standright = Spritesheet('media/enemy_1_standby_right.png').load_spritesheet(self.size, self.size)
        self.enemy_standleft = Spritesheet('media/enemy_1_standby_left.png').load_spritesheet(self.size, self.size)
        self.enemy_walkright = Spritesheet('media/enemy_1_run_right.png').load_spritesheet(self.size, self.size)
        self.enemy_walkleft = Spritesheet('media/enemy_1_run_left.png').load_spritesheet(self.size, self.size)
        self.enemy_jumpright = Spritesheet('media/enemy_1_jump_right.png').load_spritesheet(self.size, self.size)
        self.enemy_jumpleft = Spritesheet('media/enemy_1_jump_left.png').load_spritesheet(self.size, self.size)

        self.sprite = self.enemy_standright
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.hitbox_offset_x = (self.size - self.width)//2
        

        self.dir = 1
        self.moving = True
        self.jumping = 0 
        self.gravity = 0
        self.patrol = random.randint(400, 600)
        self.distance = self.patrol
        self.stay_time = 100
    
    def update(self):
        if self.jumping > 0:
            self.jumping -= 1
            for i in range(self.jumping):
                self.rect.y -= 1
            if self.dir == -1:
                self.sprite = self.enemy_jumpleft
            elif self.dir == 1:
                self.sprite = self.enemy_jumpright

    def move_around(self):
        if self.moving:
            if self.dir == 1:
                self.sprite = self.enemy_walkright
                if self.distance != 0:
                    self.distance -= 1
                    self.rect.x += self.speed
                else:
                    self.dir = -1
                    self.stay = self.stay_time
                    self.moving = False
            elif self.dir == -1:
                self.sprite = self.enemy_walkleft
                if self.distance != self.patrol:
                    self.distance += 1
                    self.rect.x -= self.speed
                else:
                    self.dir = 1
                    self.stay = self.stay_time
                    self.moving = False
        
        else:
            if self.dir == 1:
                self.sprite = self.enemy_standright
                self.stay -= 1
            elif self.dir == -1:
                self.sprite = self.enemy_standleft
                self.stay -= 1
            
            if self.stay == 0:
                self.moving = True
    
    def turn_around(self):
        self.dir *= -1

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
                self.sprite = self.enemy_jumpleft
            elif self.dir == 1:
                self.sprite = self.enemy_jumpright
    
    def hit_ground(self):
        self.gravity = 0
        self.rect.bottom = ((ceil((self.rect.bottom + 5)/BLOCK_SIZE) - 1) * BLOCK_SIZE) + 1
        return True

    def jump(self):
        if self.jumping == 0:
            self.jumping = 15     
    
    def is_jumping(self):
        return self.jumping > 0

    def reset_jump(self):
        self.jumping = 0

    def drop_health(self, damage):
        self.health -= damage

    def draw(self, off_set):
        frame = pygame.time.get_ticks() // 180 % len(self.sprite)
        screen.blit(self.sprite[frame], (self.rect.x - self.hitbox_offset_x + off_set[0], self.rect.y + off_set[1]))
        pygame.draw.rect(screen, (255, 255, 255), (self.rect.x + off_set[0], self.rect.y + off_set[1], self.rect.width, self.rect.height), 2)