import pygame
import os
import time
import random 

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
BG = pygame.image.load("files/background-black.png")

def main():
    run = True 
    FPS = 60
    clock = pygame.time.Clock()


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

main()