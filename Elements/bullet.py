import pygame as pg
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import groupcollide
from time import sleep

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship) -> None:
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        self.rect = pg.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self) -> None:
        """Move the bullet up the screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    
    def draw_bullet(self) -> None:
        """Draw the bullet to the screen."""
        pg.draw.rect(self.screen, self.color, self.rect)


class Bullets(Group):
    """A class to represent an bullets' Group."""            

    def __init__(self, ai_settings, screen, ship, aliens, stats, levels, scoreboard) -> None:
        super().__init__()

        self.settings = ai_settings
        self.screen = screen
        self.ship = ship
        self.aliens = aliens
        self.stats = stats
        self.levels = levels
        self.scoreboard = scoreboard


    def fire_bullet(self) -> None:
        """Fire a bullet if limir not reached yet."""
        if len(self) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.settings, self.screen, self.ship)
            self.add(new_bullet)

    
    def update_bullets(self) -> None:
        """Update position of bullets and get rid od old bullets."""
        self.update()

        for bullet in self:
            if bullet.rect.bottom <= 0:
                self.remove(bullet)
        
        self.check_bullet_alien()


    def check_bullet_alien(self) -> None:
        """Check if any alien collide with a bullet."""
        collisions = groupcollide(self, self.aliens, True, True)

        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points

            self.scoreboard.prep_score()
            self.stats.check_high_score()

        if len(self.aliens) == 0:
            self.empty()
            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()
            self.levels.show_level()
            sleep(3)
            self.aliens.create_fleet()