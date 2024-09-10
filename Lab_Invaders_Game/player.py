import pygame


class Player:
    """Determine img of player and his movements in the game"""
    def __init__(self, img_player_path: str):
        self.img_player = pygame.image.load(img_player_path)
        self.x = 368
        self.y = 520
        self.player_x_change = 0

    def show(self, screen: pygame.Surface) -> None:
        """Show player, update player position and ensure it stays within screen boundaries"""
        # Keep inside screen
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

        screen.blit(self.img_player, (self.x, self.y))
