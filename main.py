
from scripts.setting import *
import time as timecount
from scripts.layer import *
from scripts.game_engine import *
from scripts.menu import *


pygame.init()

clock = pygame.time.Clock()
fps = 90


class Game():
    def __init__(self):
        self.menu = Menu()
        self.game = GameEngine()
        screen_type = dict( menu = 'menu', in_game = 'in game', setting = 'setting', gameover = 'gameover')
        self.curr_screen = screen_type['in_game'] #change latter
        self.initialize_game()

    def initialize_menu(self):
        self.menu = Menu()
    def initialize_game(self):
        self.game = GameEngine()

    def update_menu(self):
        self.menu.update()
    def update_game(self):
        self.game.update()

    def draw_menu(self):
        self.menu.draw()
    def draw_game(self):
        self.game.draw()

    def button_down_menu(self, key_down):
        pass
    def button_down_game(self, key_down):
        self.game.button_down(key_down)

    def start(self):
        running = True
        while running:
            #timecount.sleep(0.1)
            clock.tick(fps)
            self.key_down = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    #self.key_down.append(event)
                    self.switch_button_down(self.curr_screen, event)

            self.switch_update(self.curr_screen)
            screen.fill((0, 0, 0))
            self.switch_draw(self.curr_screen)

            pygame.display.update()

        pygame.quit()
    
    def switch_update(self, input):
        if input == 'menu':
            self.update_menu()
        elif input == 'in game':
            self.update_game()
        return None


    def switch_draw(self, input):
        if input == 'menu':
            self.draw_menu()
        elif input == 'in game':
            self.draw_game()
        return None

    
    def switch_button_down(self, input, key):
        if input == 'menu':
            self.button_down_menu(key)
        elif input == 'in game':
            self.button_down_game(key)
        return None



newgame = Game()
newgame.start()
