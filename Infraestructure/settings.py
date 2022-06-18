import pygame as pg


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""

        # Screen settings
        self.img_bg = pg.image.load("./Images/bg.jpg")
        self.img_bg_rect = self.img_bg.get_rect()
        self.dimensions = (1200, 500)
        
        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_color = (200, 0, 30)
        self.bullets_allowed = 3

        # Aliens settings
        self.alien_speed_factor = 1
        self.alien_fleet_drop_speed = 10
        self.fleet_direction = 1

        # Game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1
        self.alien_points = 50


    def initialize_game_objects(self, screen, ship, bullets, aliens, scoreboard) -> None:
        """Get game objects."""
        self.screen = screen
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens
        self.scoreboard = scoreboard
        

    def increase_speed(self) -> None:
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    
    def background(self) -> None:
        """Draw background image."""
        self.screen.blit(self.img_bg, self.img_bg_rect)

    
    def update_screen_game(self) -> None:
        """Update images on the screen and flip to the new screen."""
        self.background()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.scoreboard.show_score()

        pg.display.flip()