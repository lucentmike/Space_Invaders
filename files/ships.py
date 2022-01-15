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

class Ship: 
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

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x,y,health=100)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

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

