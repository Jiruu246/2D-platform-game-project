
from scripts.bullet import Bullet
from scripts.setting import *
from scripts.terrain import BLOCK_SIZE
from scripts.layer import *
from scripts.map import Map
from scripts.player import PLAYER_SIZE, Player
from scripts.camera import Camera
from scripts.guns import Gun
from scripts.explode import Explode
from scripts.enemy import Enemy


class GameEngine():
    def __init__(self):
        self.map = Map()
        self.player = Player()
        self.camera = Camera(self.map)
        self.gun = Gun(self.player)
        self.bullets = []
        self.explosion = []
        self.enemies = self.map.enemies
        self.notsolid = ['Air', 'Groud_Grass', 'Lader', 'Sign', 'Small_tree']

    def update(self):
        key = pygame.key.get_pressed()
        
        self.camera.focus_on(self.player)
    
        if key[pygame.K_LEFT]: 
            self.player.dir = -1
            if not self.wall(self.player, -1):
                self.player.move_left()
        if key[pygame.K_RIGHT]:
            self.player.dir = 1
            if not self.wall(self.player, 1):
                self.player.move_right()
        if key[pygame.K_UP] and self.lader(self.player):
            self.player.climb_up()
        if key[pygame.K_DOWN] and (self.lader(self.player) or self.lader_underneath(self.player)):
            self.player.climb_down()

        if not self.lader(self.player):
            if not self.ground(self.player):
                self.player.fall()
            else:
                self.player.hit_ground()
        
        if self.player.is_jumping():
            if self.solid_overhead(self.player):
                self.player.reset_jump()
        
        self.player.update()
        self.gun.update()

        for bullet in self.bullets:
            bullet.move()
            if bullet.out_of_range() or self.wall(bullet, bullet.dir):
                self.explosion.append(Explode(bullet.rect.centerx, bullet.rect.centery))
                self.bullets.remove(bullet)

        for explosion in self.explosion:
            if explosion.finished:
                self.explosion.remove(explosion)

        for enemy in self.enemies:

            for bullet in self.bullets:
                if self.hit(enemy, bullet):
                    enemy.drop_health(bullet.damage)
                    self.explosion.append(Explode(bullet.rect.centerx, bullet.rect.centery))
                    self.bullets.remove(bullet)

            if enemy.health <= 0:
                self.enemies.remove(enemy)
            if not self.ground(enemy):
                enemy.fall()
            
            if self.onscreen(enemy.rect.x, enemy.rect.y):
                if self.ground(enemy):
                    enemy.hit_ground()

                    if self.wall_to_tall(enemy, enemy.dir):
                        if enemy.dir == -1:
                            enemy.distance = enemy.patrol
                        if enemy.dir == 1:
                            enemy.distance = 0
                        enemy.turn_around()
                    else:
                        if self.wall(enemy, enemy.dir):
                            enemy.jump()
                if enemy.is_jumping():
                    if self.solid_overhead(enemy):
                        enemy.reset_jump()

                if False:
                    pass
                else:
                    enemy.move_around()
                
            enemy.update()


    
    def draw(self):
        off_set = self.camera.view()
        self.map.draw_map(off_set)

        for bullet in self.bullets:
            bullet.draw(off_set)

        self.player.draw(off_set)
        self.gun.draw_gun(off_set)

        for explosion in self.explosion:
            explosion.draw(off_set)


    
    def ground(self, obj):
        tile_x1 = ((obj.rect.left)//BLOCK_SIZE)
        tile_x2 = ((obj.rect.right)//BLOCK_SIZE)
        tile_y = (obj.rect.bottom//BLOCK_SIZE)
        for tile_x in range(tile_x1, tile_x2 + 1):
            if self.map.tiles[tile_x][tile_y][0] not in self.notsolid:
                return True

    def wall(self, obj, dir):

        if obj.rect.right >= self.map.width * BLOCK_SIZE and dir == 1: 
            return True
        elif obj.rect.left < 0 and dir == -1:
            return True
        else:
            tiles_y1 = ((obj.rect.bottom - 2)//BLOCK_SIZE)
            tiles_y2 = ((obj.rect.top + 2)//BLOCK_SIZE)
            for tiles_y in range(tiles_y2, tiles_y1 + 1):
                if dir == -1:
                    tiles_x = (obj.rect.left//BLOCK_SIZE)
                elif dir == 1:
                    tiles_x = (obj.rect.right//BLOCK_SIZE)
                if self.map.tiles[tiles_x][tiles_y][0] not in self.notsolid:
                    return True
        return False
    

    def solid_overhead(self, obj):
        tile_x1 = ((obj.rect.left)//BLOCK_SIZE)
        tile_x2 = ((obj.rect.right)//BLOCK_SIZE)
        tiles_y = ((obj.rect.bottom)//BLOCK_SIZE)
        for tile_x in range(tile_x1, tile_x2 + 1):
            if self.map.tiles[tile_x][tiles_y -2][0] not in self.notsolid:
                return True
    
    def lader(self, obj):
        tiles_x = (obj.rect.centerx//BLOCK_SIZE)
        tiles_y = ((obj.rect.bottom - 3)//BLOCK_SIZE)
        return self.map.tiles[tiles_x][tiles_y][0] == 'Lader'
    
    def lader_underneath(self, obj):
        tiles_x = (obj.rect.centerx//BLOCK_SIZE)
        tiles_y = ((obj.rect.bottom - 2)//BLOCK_SIZE)
        return self.map.tiles[tiles_x][tiles_y + 1][0] == 'Lader'
    
    def onscreen(self, x, y):
        if x in range(self.camera.off_set_x - 100, self.camera.off_set_x + screen_width + 200) and y in range(self.camera.off_set_y - 100, self.camera.off_set_y + screen_height + 100): # 100 and 200 are pre-load out side the range so other movement will apear smoother
            return True
        else:
            return False
    
    def wall_to_tall(self, obj, dir):
        if obj.rect.right >= self.map.width * BLOCK_SIZE and dir == 1: 
            return True
        elif obj.rect.left < 0 and dir == -1:
            return True
        else:
            tiles_y = ((obj.rect.bottom - 2)//BLOCK_SIZE)
            if dir == -1:
                tiles_x = (obj.rect.left//BLOCK_SIZE)
            elif dir == 1:
                tiles_x = (obj.rect.right//BLOCK_SIZE)
            if self.map.tiles[tiles_x][tiles_y - 1][0] not in self.notsolid:
                return True
        return False
    
    def hit(self, obj1, obj2):
        if obj1.rect.colliderect(obj2.rect):
            return True
        else:
            return False


    def button_down(self, key_down):
        if key_down.key == pygame.K_UP and not self.lader(self.player):
            if self.ground(self.player):
                self.player.jump()
        if key_down.key == pygame.K_SPACE:
            bullet = Bullet(self.gun.rect.right, self.gun.rect.centery, self.gun.dir)
            self.bullets.append(bullet)


        
    