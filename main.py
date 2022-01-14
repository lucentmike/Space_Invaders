import pygame
import os
import time
import random 
from files.ships import Ship
pygame.font.init()

#Create pygame window and set width and height

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

#Load images
RED_SPACE_SHIP = pygame.image.load("files/pixel_ship_red_small.png")
BLUE_SPACE_SHIP = pygame.image.load("files/pixel_ship_blue_small.png")
GREEN_SPACE_SHIP = pygame.image.load("files/pixel_ship_green_small.png")

#Player ship
YELLOW_SPACE_SHIP = pygame.image.load("files/pixel_ship_yellow.png")

#Lasers
RED_LASER = pygame.image.load("files/pixel_laser_red.png")
GREEN_LASER = pygame.image.load("files/pixel_laser_green.png")
BLUE_LASER = pygame.image.load("files/pixel_laser_blue.png")
YELLOW_LASER = pygame.image.load("files/pixel_laser_yellow.png")

#Background
BG = pygame.transform.scale(pygame.image.load("files/invaders.png"), (WIDTH, HEIGHT))

def main():
    run = True 
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    ship = Ship(300, 650)

    player_vel = 5

    clock = pygame.time.Clock()

    def redraw_window():
        #Draw background
        WIN.blit(BG, (0,0))

        #Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10 ))

        #Drawe ships from the Ships class
        ship.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
        #Use keys method to find out which keys are pressed and assign action
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:#moving left
            ship.x -= player_vel 
        if keys[pygame.K_d]: #moving right
            ship.x += player_vel
        if keys[pygame.K_w]: #moving up 
            ship.y -= player_vel 
        if keys[pygame.K_s]: #moving down
            ship.y += player_vel

main()