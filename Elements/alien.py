import pygame as pg
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame.sprite import spritecollideany

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = screen
        self.settings = ai_settings

        self.image = pg.image.load("Images/alien.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


    def blitme(self) -> None:
        """Draw the alien at its current location."""        
        self.screen.blit(self.image, self.rect)

    
    def update(self) -> None:
        """Move the alien right."""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x


    def check_edges(self) -> bool:
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


class Aliens(Group):
    """A class to represent an alien's Group."""            

    def __init__(self, ai_settings, screen, ship) -> None:
        super().__init__()
        
        self.settings = ai_settings
        self.screen = screen
        self.ship = ship

        self.screen_rect = self.screen.get_rect()


    def create_alien(self, alien_number, row_number) -> None:    
        """Create an alien and place it in the row."""
        alien = Alien(self.settings, self.screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.add(alien)

    
    def update_aliens(self) -> None:
        """Update the positions of all aliens in the fleet."""
        self.check_fleet_edges()
        self.update()

        if spritecollideany(self.ship, self):
            self.ship.ship_hit()

        self.check_aliens_bottom()


    def check_aliens_bottom(self) -> bool:
        """Check if any aliens have reached the bottom of the screen."""
        reached_bottom = False
        for alien in self.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                reached_bottom = True
                break
        
        return reached_bottom

    
    def check_fleet_edges(self) -> bool:
        """Respond appropriately if any aliens have reched an edge."""
        for alien in self.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break


    def get_number_rows(self, ship_height, alien_height) -> int:
        """Determine the number of rows of aliens that fit on the screen."""
        available_space_y = (self.settings.dimensions[1] - (3*alien_height) - ship_height)
        number_rows = int(available_space_y / (2*alien_height))

        return number_rows


    def get_number_aliens_x(self, alien_width) -> int:
        """Determine the number os aliens that fit in a row."""
        available_space_x = self.settings.dimensions[0] - 2 * alien_width
        number_aliens_x = int(available_space_x/(2*alien_width))

        return number_aliens_x


    def create_fleet(self) -> None:
        """Create a full fleet of aliens."""
        alien = Alien(self.settings, self.screen)
        number_aliens_x = self.get_number_aliens_x(alien.rect.width)
        number_rows = self.get_number_rows(self.ship.rect.height, alien.rect.height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)


    def change_fleet_direction(self) -> None:
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.sprites():
            alien.rect.y += self.settings.alien_fleet_drop_speed

        self.settings.fleet_direction *= -1