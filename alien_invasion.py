import pygame as pg

from Infraestructure.events import AiEvents
from Infraestructure.settings import Settings
from Infraestructure.game_stats import GameStats

from Elements.ship import Ship
from Elements.alien import Aliens
from Elements.bullet import Bullets
from Elements.scoreboard import Scoreboard
from Elements.levels import Levels
from Pages.highscore import HighscorePage

from Pages.start_page import StartPage
from Pages.nickname import Nickname
from Pages.highscore import HighscorePage

from Database.highscores import Highscores


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(self.settings.dimensions)

        self.highscores = Highscores()
        self.stats = GameStats(self.settings)
        self.nickname = Nickname(self.screen, self.stats)
        self.ship = Ship(self.settings, self.screen)
        self.aliens = Aliens(self.settings, self.screen, self.ship)
        self.levels = Levels(self.settings, self.screen, self.stats)
        self.sb = Scoreboard(self.settings, self.screen, self.stats)
        self.bullets = Bullets(self.settings, self.screen, self.ship, self.aliens, self.stats, self.levels, self.sb)
        self.start_page = StartPage(self.settings, self.screen, self.highscores)
        self.highscores_page = HighscorePage(self.screen, self.settings, self.highscores)
        self.ai_events = AiEvents(self.screen, self.settings, self.sb, self.stats, self.ship, self.aliens, self.bullets, self.start_page, self.highscores, self.nickname)
        
        self.stats.add_scoreboard(self.sb)
        self.ship.add_dynamic_parameters(self.stats, self.aliens, self.bullets, self.sb, self.highscores)
        self.settings.initialize_game_objects(self.screen, self.ship, self.bullets, self.aliens, self.sb)
        pg.display.set_caption("Alien Invasion")
        
    
    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self.ai_events.check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update_bullets()
                self.aliens.update_aliens()
                self.settings.update_screen_game()
            elif self.stats.highscores_display:
                self.highscores_page.draw_highscores()
                pg.display.flip()
            else:
                self.start_page.display()


if __name__ == "__main__":
    alien_invasion = AlienInvasion()

    alien_invasion.run_game()