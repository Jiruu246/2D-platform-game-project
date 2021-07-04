import pygame

class Spritesheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()

    def load_spritesheet(self, width, height, scale = 1, color=(0,0,0)):
        sprite_list = []
        spritesheet_height = self.sprite_sheet.get_height()
        spritesheet_width = self.sprite_sheet.get_width()
        y = 0
        i = 0
        while y < spritesheet_height:
            x = 0
            while x < spritesheet_width:
                image = pygame.Surface((width, height)).convert_alpha()
                image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
                image = pygame.transform.scale(image, (width * scale, height * scale))
                image.set_colorkey(color)
                sprite_list.append(image)
                x += width
            y += height
        return sprite_list