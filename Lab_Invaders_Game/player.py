import pygame



class Player:
    def __init__(self, img_player_path: str, ):
        self.img_player = pygame.image.load(img_player_path)
        self.x = 368  # our screen width = 800, half_screen = 400, object = 64 px, so 400-32=368
        self.y = 520  # our screen hight = 600, to place on the bottom of the screen  600-64=536
        self.player_x_change = 0

    def show(self, screen):
        """Show player on screen"""
        # Keep inside screen
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

        screen.blit(self.img_player, (self.x, self.y))

