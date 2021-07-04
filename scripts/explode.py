from scripts.setting import *
from scripts.sprtiesheet import Spritesheet
from scripts.layer import *

class Explode(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size = 20
        self.explode = Spritesheet('media/effect.png').load_spritesheet(self.size, self.size)
        self.rect = self.explode[0].get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.img_index = 0
        self.finished = False

    def draw(self, off_set):
        if self.img_index < len(self.explode):
            screen.blit(self.explode[self.img_index], (self.rect.x + off_set[0], self.rect.y + 10 + off_set[1]))
            #pygame.draw.rect(screen, (255, 255, 255), (self.rect.x + off_set[0], self.rect.y + off_set[1], self.rect.width, self.rect.height), 2)
            self.img_index += 1
        else:
            self.finished = True