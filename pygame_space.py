import random
import pygame
import math
#initialize
screen_width=800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collision_distance=27
#init
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
background=pygame.image.load("Game_Background.png")

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('game.icon-removebg-preview.png')
pygame.display.set_icon(icon)
# Player
playerlmg = pygame.image.load('game.rocket-removebg-preview.png')
playerX = player_start_x
playerY = player_start_y
playerX_change = 0
# Enemy
enemylmg =[]
enemyX=[]
enemyY = []
enemyX_change =[]
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
     enemylmg.append(pygame.image.load('pngtree-ufo-3d-model-transparent-background-image-png-image_15146313-removebg-preview.png'))
     enemyX.append(random.randint(0, screen_width- 64)) # 64 is the size of the enemy
     enemyY.append(random.randint(enemy_start_y_min,enemy_start_y_max))
     enemyX_change.append(enemy_speed_x)
     enemyY_change.append(enemy_speed_y)
# Bullet
bulletlmg = pygame.image.load('game.bullet-removebg-preview.png')
bulletX = 0
bulletY = player_start_y
bulletX_change = 0
bulletY_change = bullet_speed_y
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x,y):
  score = font.render("Score : "+ str(score_value), True, (255, 255, 255))
  screen.blit(score, (x,y))

def game_over_text():
  over_text = over_font.render("GAME OVER", True, (255, 255, 255))
  screen.blit(over_text, (200, 250))

def player(x, y):
  screen.blit(playerlmg, (x, y))
def enemy(x, y, i):
# Draw an enemy on the screen
  screen.blit(enemylmg[i], (x, y))
def fire_bullet(x, y):
# Fire a bullet from the player's position
 global bullet_state
 bullet_state = "fire"
 screen.blit(bulletlmg, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
# Check if there is a collision between the enemy and a bullet
   distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) * 2)
   return distance < collision_distance
#Game loop
running = True
while running:
  screen.fill((0, 0, 0))
  screen.blit(background, (0, 0))
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     running = False
   if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_LEFT:
       playerX_change =- 5
     if event.key == pygame.K_RIGHT:
       playerX_change = 5
     if event.key == pygame.K_SPACE and bullet_state == "ready":
       bulletX = playerX
       fire_bullet(bulletX, bulletY)
   if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
     playerX_change = 0
# Player Movement
  playerX += playerX_change
  playerX = max(0, min(playerX, screen_width - 64)) # 64 is the size of the player
  # Enemy Movement
  for i in range(num_of_enemies):
   if enemyY[i] > 340: # Game Over Condition
     for j in range(num_of_enemies):
      enemyY[j] =2000
     game_over_text()
     break
   enemyX[i] += enemyX_change[i]
   if enemyX[i] <= 0 or enemyX[i]>= screen_width - 64:
    enemyX_change[i] *=- 1
    enemyY[i] += enemyY_change[i]
# Collision Check
   if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
     bulletY = player_start_y
     bullet_state = "ready"
     score_value +=1
     enemyX[i] = random.randint(0, screen_width - 64)
     enemyY[i] = random.randint(enemy_start_y_min, enemy_start_y_max)
   enemy(enemyX[i], enemyY[i], i)
# Bullet Movement
  if bulletY <= 0:
    bulletY = player_start_y
    bullet_state = "ready"
  elif bullet_state == "fire":
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change
  player(playerX, playerY)
  show_score(textX, textY)
  pygame.display.update()