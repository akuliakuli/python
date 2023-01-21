import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800,600))

# player image
player_img = pygame.image.load("spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0

alien_img = pygame.image.load("alien.png")
alien_x = random.randint(0,800)
alien_y = random.randint(50,150)
alien_x_change = 0.3
alien_y_change = 40


pygame.display.set_caption("Space Battle")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
    


def draw_object(img,x,y):
    screen.blit(img,(x,y))


running = True
while running:
    screen.fill((0,51,102))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change += -0.3
            if event.key == pygame.K_RIGHT:
                player_x_change += 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_change = 0
            if event.key == pygame.K_RIGHT:
                player_x_change = 0
    

    player_x += player_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    alien_x += alien_x_change

    if alien_x <= 0:
        alien_x_change = 0.25
        alien_y += alien_y_change
    elif alien_x >= 736:
        alien_x_change = -0.25
        alien_y += alien_y_change


    draw_object(player_img,player_x,player_y)
    draw_object(alien_img,alien_x,alien_y)
    pygame.display.update()
