import pygame


class Score:
    def __init__(self):
        self.score = 0
        self.score_font = pygame.font.Font('assets/font/SaucerBB.ttf', 30)  # https://www.1001freefonts.com/

    def show(self, screen):
        """Show score on screen"""
        text = self.score_font.render(f"Score: {self.score}", True, (37, 121, 104))
        screen.blit(text, (10, 10))
