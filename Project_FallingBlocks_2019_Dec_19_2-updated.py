# 2nd session at Falling Block
# 2019 December 18th

import pygame
import random
import sys
import math

pygame.init()
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

Width = 520
Height = 600

screen = pygame.display.set_mode((Width, Height))
caption = pygame.display.set_caption('Falling Block Alpha 1.1.0')

pygame.font.get_fonts()
font = pygame.font.SysFont('arialms', 25)

game_over = False
FPS = 20
score = 0
vel = 5
player_pos = [Width/2-25, Height/2-25, 50, 50]
number_enemies = 6
enemy_pos = [random.randint(0, Width-50), 0]
enemy_list = [enemy_pos]

def add_enemies(enemy_list):
    duration = random.random()
    if len(enemy_list) < number_enemies and duration < 0.2:
        enemy_list.append([random.randint(0, Width-50), 0])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos, (50, 50)))

def update_enemies(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >=0 and enemy_pos[1] < Height:
            enemy_pos[1] += vel
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def detect_collision(enemy_list):
    for enemy_pos in enemy_list:
        if check_collision(enemy_pos[0], enemy_pos[1], player_pos[0], player_pos[1]):
            return True
    return False

# def create_enemy(ex,ey,score):
#     enemy = pygame.draw.rect(screen, BLUE, (ex, ey, 50, 50))
#     if ey >= 0 and ey <= Height:
#         if score <= 20:
#                 ey += 20
#         else:
#                 ey += vel
#     else:
#         ex = random.randint(0,Width-50)
#         ey = 0
#         score += 1

def check_collision(ex,ey,px,py):
    if math.fabs(px-ex) < 50 and math.fabs(py-ey) < 50:
        return True
    return False   

# def enemy_list(number_enemies,px,py):
#     enemies = []
#     ex = random.randint(0, Width-50)
#     ey = 0
#     for i in range (number_enemies):
#         enemies.append(create_enemy(ex,ey,score))
#         if check_collision(ex,ey,px,py) == True:
#             return True

def set_level(score, vel):
    if score < 20:
        vel = 10
    elif score < 40:
        vel = 20
    else:
        vel = score/2
    return vel

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > vel:
        player_pos[0] -= vel
    if keys[pygame.K_RIGHT] and player_pos[0] < Width-vel-50:
        player_pos[0] += vel
    if keys[pygame.K_UP] and player_pos[1] > vel:
        player_pos[1] -= vel
    if keys[pygame.K_DOWN] and player_pos[1] < Height-vel-50:
        player_pos[1] += vel
    if keys[pygame.K_ESCAPE]:
        game_over = True

    player_pos = [player_pos[0], player_pos[1]]
    player = pygame.draw.rect(screen, RED, (player_pos, (50, 50)))
    # enemy_list(number_enemies,player_pos[0],player_pos[1])

    add_enemies(enemy_list)
    score = update_enemies(enemy_list, score)
    vel = set_level(score, vel)
    draw_enemies(enemy_list)
    if detect_collision(enemy_list):
        print("Total score: " + str(score))
        print("Final speed: " + str(vel))
        game_over = True

    text = font.render('Your Score is: '+str(score), True, WHITE)
    center_text = Width/2-text.get_rect().width/2
    screen.blit(text, [center_text, 50])
    pygame.display.update()
    screen.fill(BLACK)
    clock.tick(FPS)
