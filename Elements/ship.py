import pygame as pg
from pygame.sprite import Sprite
from time import sleep

class Ship(Sprite):
    """A class to manage the ship."""

    
    def __init__(self, ai_settings, screen) -> None:
        """Initialize the ship and set its starting position."""
        super().__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        self.image = pg.image.load("Images/ship.png")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def add_dynamic_parameters(self, stats, aliens, bullets, scoreboard, high_score_db) -> None:
        """Initialize special parameters."""
        self.stats = stats
        self.aliens = aliens
        self.bullets = bullets
        self.scoreboard = scoreboard
        self.high_score_db = high_score_db
    

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        

    def update(self) -> None:
        """Update the ship's position based on the movement."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def center_ship(self) -> None:
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx


    def ship_hit(self) -> None:
        """Respond to ship hit by alien."""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.scoreboard.prep_ship()

            self.aliens.empty()
            self.bullets.empty()

            self.aliens.create_fleet()
            self.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            self.high_score_db.save(self.stats.high_score, self.stats.nickname)