import pygame
import random


class Enemy():
    """Define img and number of enemies in game"""

    def __init__(self, img_enemy: list[str], num_of_enemies: int = 8):
        # super().__init__()
        self.img_paths = img_enemy
        self.img_enemy = []
        self.number_of_enemies = num_of_enemies
        self.enemy_x = []
        self.enemy_y = []
        self.enemy_x_change = []
        self.enemy_y_change = []
        self.end_game_font = pygame.font.Font("assets/font/SaucerBB.ttf", 40)

    def create_enemies(self):
        for e in range(self.number_of_enemies):
            self.img_enemy.append(pygame.image.load(random.choice(self.img_paths)))
            self.enemy_x.append(random.randint(0, 736))
            self.enemy_y.append(random.randint(50, 200))
            self.enemy_x_change.append(0.8)
            self.enemy_y_change.append(50)


    def show_enemy(self, x, y, en, screen):
        screen.blit(self.img_enemy[en], (x, y))

    def move(self, screen):
        """Modify enemy location """
        for enem in range(self.number_of_enemies):
            # Define end of game when enemy too close
            if self.enemy_y[enem] > 450:
                for k in range(self.number_of_enemies):
                    self.enemy_y[k] = 1000
                my_final_font = self.end_game_font.render('GAME OVER', True, (162, 13, 13))
                screen.blit(my_final_font, (250, 250))
                break
            self.enemy_x[enem] += self.enemy_x_change[enem]

            # Keep enemy inside screen
            if self.enemy_x[enem] <= 0:
                self.enemy_x_change[enem] = 0.3
                self.enemy_y[enem] += self.enemy_y_change[enem]
            elif self.enemy_x[enem] >= 736:
                self.enemy_x_change[enem] = -0.3
                self.enemy_y[enem] += self.enemy_y_change[enem]

