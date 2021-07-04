from scripts.setting import *
from scripts.layer import screen_width, screen_height
from scripts.terrain import BLOCK_SIZE

class Camera():
    def __init__(self, map):
        self.map = map
        self.off_set_x = self.off_set_y = 0
    
    def focus_on(self, obj):
        self.off_set_x = min(max(obj.rect.x - screen_width // 2, 0), self.map.width * BLOCK_SIZE - screen_width)
        self.off_set_y = min(max(obj.rect.y - screen_height // 2, 0), self.map.height * BLOCK_SIZE - screen_height)

        #print(self.off_set_x)

    def view(self):
        return [-(self.off_set_x + 200), -(self.off_set_y - 50)]