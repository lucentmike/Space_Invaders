import imghdr
import pygame

#Load images
RED_SPACE_SHIP = pygame.image.load("files/pixel_ship_red_small.png")
BLUE_SPACE_SHIP = pygame.image.load("files/pixel_ship_blue_small.png")
GREEN_SPACE_SHIP = pygame.image.load("files/pixel_ship_green_small.png")

#Player ship
YELLOW_SPACE_SHIP = pygame.image.load("files/pixel_ship_yellow1.png")

#Lasers
RED_LASER = pygame.image.load("files/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("files/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("files/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("files/pixel_laser_yellow.png")

#Background

WIDTH, HEIGHT = 750, 750

#creates a collide function that detects is pixels overlap
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

#creates laser class
class Laser:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move (self, vel):
        self.y += vel

    def off_screen(self, height):
        return not self.y <= height and self.y >= 0

    def collision(self, obj):
        return collide(obj, self)

class Ship: 

    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health 
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0 

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y-50, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1
    

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x,y,health=100)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
               for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)  

    def laser_collide(self, objs):
        for laser in self.lasers:
            for obj in objs:
                if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)                                                                                      

    #health bar that green side dcrements with player calss
    def health_bar(self, window):
        pygame.draw.rect(window, (255,0,0,), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0,), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

    def draw(self, window):
        super().draw(window)
        self.health_bar(window)

class Enemy(Ship):

    COLOR_MAP = {
        "red":(RED_SPACE_SHIP, RED_LASER), 
        "green":(GREEN_SPACE_SHIP, GREEN_LASER), 
        "blue":(BLUE_SPACE_SHIP, BLUE_LASER)
        }

    def __init__(self, x, y, color, health =100):
        super().__init__(x,y,health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):

        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


