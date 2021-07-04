
from scripts.setting import *
from scripts.layer import *
from scripts.sprtiesheet import Spritesheet


class Gun:
    def __init__(self, player, gun_size=60):
        self.player = player
        self.gun_size = gun_size
        self.guns = Spritesheet('media/guns.png').load_spritesheet(self.gun_size, self.gun_size)
        self.rect = self.guns[0].get_rect()
        self.off_set_x = 40

    def update(self):
        self.dir = self.player.dir
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y


    def draw_gun(self, off_set):

        frame = pygame.time.get_ticks() // 180 % len(self.guns)

        if self.dir == 1:
            gun_img = self.guns[frame]
            self.off_set_x = 35
        elif self.dir == -1:
            gun_img = pygame.transform.flip(self.guns[frame], True, False).convert_alpha()
            self.off_set_x = 0

        screen.blit(gun_img, (self.rect.x + self.off_set_x + off_set[0], self.rect.y + 30 + off_set[1]))
        #pygame.draw.rect(screen, (255, 255, 255), (self.rect.x + self.off_set_x + off_set[0], self.rect.y + 30 + off_set[1], self.rect.width, self.rect.height), 2)