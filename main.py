from tkinter import N
import pygame
import os
import time
import random 
from files.ships import Enemy, Ship, Player, Laser, collide
pygame.font.init()

#Create pygame window and set width and height

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

BG = pygame.transform.scale(pygame.image.load("files/invaders.png"), (WIDTH, HEIGHT))
BG2 = pygame.transform.scale(pygame.image.load("files/background-black.png"), (WIDTH, HEIGHT))
BG3 = pygame.transform.scale(pygame.image.load("files/background-new.jpeg"), (WIDTH, HEIGHT))



LOGO = pygame.transform.scale(pygame.image.load("files/logo.png"), (WIDTH - 100, HEIGHT ))

def main():
    run = True 
    FPS = 60
    level = 0

    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 70)

    enemies = []
    wave_legnth = 0
    enemey_vel = 1

    player = Player(300, 630)

    player_vel = 5
    laser_vel = 5

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        #Draw background

        if level > 2 :
            WIN.blit(BG2, (0,0))
        elif level > 1 < 3:
            WIN.blit(BG3, (0,0))
        else:
            WIN.blit(BG, (0,0))

        #Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10 ))

        #Draw ships from the Ships class

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)
  
        #If lost is True, return the you lost label
        if lost:
            lost_label = lost_font.render("You Lost!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        
        #If live is 0 or zero health, turn list boolean to True 
        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        #If lost is True, run timer and quit game. 
        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        #Span enemies when enemies is 0, with random placement and color and place in list. Spawns 5 enenmies when list is 0 and incriments the level
        if len(enemies) == 0:
            level +=1
            wave_legnth += 5
            for i in range (wave_legnth):
                enemy = Enemy(random.randrange(50, WIDTH -100), random.randrange(-750, -100), random.choice(["red", "blue", "green"]), )
                enemies.append(enemy)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        #Use keys method to find out which keys are pressed and assign action
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:#moving left
            player.x -= player_vel 
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: #moving right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: #moving up 
            player.y -= player_vel 
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: #moving down
            player.y += player_vel
        if keys[pygame.K_SPACE]: #shoots lasers
            player.shoot()

        #Moves the enemies down, and shoots shoots enemy lasers
        for enemy in enemies[:]:
            enemy.move(enemey_vel)
            enemy.move_lasers(laser_vel, player)

            if enemy.y >= 0:
                if random.randrange(0, 360) == 1:
                    enemy.shoot()
            
            #decrements player health if collision
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
                
            #removes enemy from scneen if off screen
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -=1 
                enemies.remove(enemy)

        #moves the player laser
        player.move_lasers(-laser_vel, enemies)

        for enemy in enemies:
            player.laser_collide(enemy.lasers)

#Creates a main menu, if button is presses start game, x is presses program is exited
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 40)
    run = True
    while run:
        WIN.blit (BG, (0,0))
        WIN.blit (LOGO, (WIDTH/2 - LOGO.get_width()/2, -200))
        title_label = title_font.render("Press the mouse button to begin", 1, (255, 255, 255))
        controls = title_font.render("Move: AWSD | Shoot: Space", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        WIN.blit(controls, (WIDTH/2 - title_label.get_width()/2 + 30, 400))


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()