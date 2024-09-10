import pygame


class Score:
    """Count and display the score in the game."""
    def __init__(self):
        self.score = 0
        self.score_font = pygame.font.Font('assets/font/SaucerBB.ttf', 30)  # https://www.1001freefonts.com/

    def show(self, screen: pygame.Surface) -> None:
        """Render and display the score on the screen."""
        text = self.score_font.render(f"Score: {self.score}", True, (37, 121, 104))
        screen.blit(text, (10, 10))
