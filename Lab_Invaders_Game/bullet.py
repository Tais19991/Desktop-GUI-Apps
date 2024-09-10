import pygame
import math


class Bullet:
    def __init__(self, img_bullet_path: str):
        self.img_bullet = pygame.image.load(img_bullet_path)
        self.x = 0
        self.y = 500
        self.x_change = 0
        self.y_change = 0.7
        self.visible = False

    def shoot(self, screen, x, y):
        """Shoot bullet from player """
        self.visible = True
        screen.blit(self.img_bullet, (x + 16, y + 10))

    def move(self, screen):
        if self.y <= -64:
            self.y = 500
            self.visible = False
        if self.visible:
            self.shoot(screen, self.x, self.y)
            self.y -= self.y_change

    def there_is_a_collision(self, x_enemy, y_enemy):
        distance = math.sqrt(math.pow(x_enemy - self.x, 2) + math.pow(self.y - y_enemy, 2))
        if distance < 42:
            return True
        else:
            return False