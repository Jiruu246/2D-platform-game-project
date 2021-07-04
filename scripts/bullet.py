from scripts.setting import *
from scripts.layer import *
from scripts.sprtiesheet import Spritesheet

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dir):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_size = 20
        self.bullet = Spritesheet('media/bullet.png').load_spritesheet(self.bullet_size, self.bullet_size)
        self.rect = self.bullet[0].get_rect()
        self.damage = 1
        self.speed = 15
        self.rect.x = x
        self.rect.y = y        
        self.start_x = x
        self.dir = dir
        self.range = 500
    
    def move(self):
        if self.dir == 1:
            self.rect.x += self.speed
        elif self.dir == -1:
            self.rect.x -= self.speed

    def draw(self, off_set):
        frame = pygame.time.get_ticks() // 180 % len(self.bullet)

        if self.dir == 1:
            bullet_img = self.bullet[frame]
        elif self.dir == -1:
            bullet_img = pygame.transform.flip(self.bullet[frame], True, False).convert_alpha()
        
        screen.blit(bullet_img, (self.rect.x + off_set[0], self.rect.y + 10 + off_set[1]))
        pygame.draw.rect(screen, (255, 255, 255), (self.rect.x + off_set[0], self.rect.y + 10 + off_set[1], self.rect.width, self.rect.height), 1)

    def out_of_range(self):
        if self.dir == 1:
            return self.rect.x > (self.start_x + self.range)
        elif self.dir == -1:
            return self.rect.x < (self.start_x - self.range)