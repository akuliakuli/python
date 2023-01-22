import pygame
import random
import math 

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

bullet_img = pygame.image.load("laser.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 0.8

bullet_state = "ready"

pygame.display.set_caption("Space Battle")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
    


def draw_object(img,x,y):
    screen.blit(img,(x,y))

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
    collision = math.sqrt((math.pow(enemy_x - bullet_x,2)) + (math.pow(enemy_y - bullet_y,2)) )
    return collision < 27 


def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x + 16 ,y + 10))
score = 0
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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire(bullet_x,bullet_y)

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

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"   
    if bullet_state == "fire":
        fire(bullet_x,bullet_y)
        bullet_y -= bullet_y_change

    collision = is_collision(alien_x,alien_y,bullet_x,bullet_y)
    if collision:
        bullet_y = 480
        bullet_state = "ready"
        score += 1
        print(score)
        alien_x = random.randint(0,735)
        alien_y = random.randint(50,150)
 
    draw_object(player_img,player_x,player_y)
    draw_object(alien_img,alien_x,alien_y)
    pygame.display.update()
