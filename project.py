import pygame
import random
import math 

from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((800,600))


# player image
player_img = pygame.image.load("spaceship.png")
player_x = 370
player_y = 480
player_x_change = 0

alien_count = 7
alien_img = []
alien_x = []
alien_y = []
alien_x_change = []
alien_y_change = []


for i in range(alien_count):
    alien_img.append(pygame.image.load("alien.png"))
    alien_x.append(random.randint(0,800))
    alien_y.append(random.randint(50,150))
    alien_x_change.append(0.3)
    alien_y_change.append(40)

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

def draw_enemy(enemyimg,x,y,i):
    screen.blit(enemyimg[i],(x,y))

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
    collision = math.sqrt((math.pow(enemy_x - bullet_x,2)) + (math.pow(enemy_y - bullet_y,2)) )
    return collision < 27 


def fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img,(x + 16 ,y + 10))


score_value = 0

font = pygame.font.Font("FRUIT-ACID.ttf",42)

game_over_font = pygame.font.Font("FRUIT-ACID.ttf",64)

text_x = 10
text_y = 10
def render_text(x,y):
    score = font.render(f"Score : {str(score_value)}",True,(255,255,255))
    screen.blit(score,(x,y))


running = True

def game_over_text():
    score = game_over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(score,(210,100))


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
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
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

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"   
    if bullet_state == "fire":
        fire(bullet_x,bullet_y)
        bullet_y -= bullet_y_change

    for i in range(alien_count):
        if alien_y[i] > 440:
            for j in range(alien_count):
                alien_y[i] = 2000
            game_over_text()
            break
        alien_x[i] += alien_x_change[i]
        if alien_x[i] <= 0:
            alien_x_change[i] = 0.25
            alien_y[i] += alien_y_change[i]
        elif alien_x[i] >= 736:
            alien_x_change[i] = -0.25
            alien_y[i] += alien_y_change[i]

        
        collision = is_collision(alien_x[i],alien_y[i],bullet_x,bullet_y)
        if collision:
            collision_sound = mixer.Sound("explosion.wav")
            collision_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            alien_x[i] = random.randint(0,735)
            alien_y[i] = random.randint(50,150)
        draw_enemy(alien_img,alien_x[i],alien_y[i],i)

    render_text(text_x,text_y)
    draw_object(player_img,player_x,player_y)
    pygame.display.update()
