import pygame
import math
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('background.jpg')

# icon
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# title
pygame.display.set_caption("Space Invaders!")

# player
playerimg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemy = 6

# enemy
for i in range(number_of_enemy):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,100))
    enemyX_change.append(0.2)
    enemyY_change.append(32)

# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_status = "ready"

#score
score_value = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)
textX = 10
textY = 10

#game_over
go_font = pygame.font.SysFont('freesansbold.ttf', 140)

def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bulletimg, (x, y - 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    dX = (math.pow((enemyX - bulletX), 2))
    dY = (math.pow((enemyY - bulletY), 2))
    distance = math.sqrt(dX + dY)
    if distance < 27:
        return True
    else:
        return False

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over():
    go = font.render("GAME OVER", True, (255,255,255))
    screen.blit(go, (290, 300))

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_status == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerX += playerX_change

    for i in range(number_of_enemy):
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.2
            enemyY[i] += enemyY_change[i]

        enemyX[i] += enemyX_change[i]

        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_status = "ready"
            score_value += 1
            enemyX[i] = 0
            enemyY[i] = 0

        enemy(enemyX[i], enemyY[i], i)

        if enemyY[i] > 440:
            for j in range(number_of_enemy):
                enemyY[j] = 800
            game_over()
            break

    if bulletY <= 0:
        bulletY = 480
        bullet_status = "ready"

    if bullet_status == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
