import pygame
import random
from pygame import mixer
from enemy import Enemy
from player import Player
from bullet import Bullet
from score import Score


# Initialise pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("Lab Invasion")
icon = pygame.image.load('assets/mouse.png')
pygame.display.set_icon(icon)
background = pygame.image.load("assets/green_lab.jpg")

# Add music
mixer.music.load('assets/music/backmu.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

# Classes initialisation
player = Player(img_player_path='assets/player.png')
enemies = Enemy(img_enemy=['assets/prof84.png', 'assets/sci2.png'], num_of_enemies=7)
enemies.create_enemies()
bullet = Bullet(img_bullet_path='assets/poop.png')
score = Score()

# ----------------------------------------------------GAME LOOP-----------------------------------------------
is_running = True

while is_running:
    screen.fill((186, 152, 219))
    screen.blit(background, (0, 0))

    # Event iteration
    for event in pygame.event.get():

        # Closing Event
        if event.type == pygame.QUIT:
            is_running = False

        # Press arrow key event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_x_change = -0.3
            if event.key == pygame.K_RIGHT:
                player.player_x_change = 0.3
            if event.key == pygame.K_SPACE:
                bullet_sound = mixer.Sound('assets/music/shot.mp3')
                bullet_sound.play()
                mixer.music.set_volume(0.5)
                if not bullet.visible:
                    bullet.x = player.x
                    bullet.shoot(x=player.x, y=bullet.y, screen=screen)

        # Release key event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_x_change = 0

    # Modify player location
    player.x += player.player_x_change
    # Move enemies
    enemies.move(screen)

    # Collision
    for enemy_num in range(enemies.number_of_enemies):
        collision = bullet.there_is_a_collision(enemies.enemy_x[enemy_num], enemies.enemy_y[enemy_num])

        if collision:
            collision_sound = mixer.Sound('assets/music/punch.mp3')
            collision_sound.play()
            bullet.y = 500
            bullet.visible = False
            score.score += 1
            enemies.enemy_x[enemy_num] = random.randint(0, 736)
            enemies.enemy_y[enemy_num] = random.randint(50, 200)
        enemies.show_enemy(enemies.enemy_x[enemy_num], enemies.enemy_y[enemy_num], enemy_num, screen)

    bullet.move(screen)
    player.show(screen)
    score.show(screen)
    pygame.display.update()
