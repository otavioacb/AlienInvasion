import pygame as pg
import sys 
from Componets.text import Text

class AiEvents:
    """A class to manage game events."""

    def __init__(self, screen, ai_settings, scoreboard, stats, ship, aliens, bullets, start_page, highscore_db, nickname) -> None:
        self.screen = screen
        self.settings = ai_settings
        self.scoreboard = scoreboard
        self.stats = stats
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets
        self.start_page = start_page
        self.highscore_db = highscore_db
        self.nickname = nickname


    def check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.highscore_db.con.close()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.check_button(mouse_x, mouse_y)


    def check_keyup_events(self, event) -> None:
        """Responde to key releases."""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False


    def check_keydown_events(self, event) -> None:
        """Respond to keypresses."""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_SPACE:
            self.bullets.fire_bullet()
        elif event.key == pg.K_q and pg.key.get_mods() & pg.KMOD_SHIFT:
            self.highscore_db.con.close()
            sys.exit()
        elif event.key == pg.K_a and pg.key.get_mods() & pg.KMOD_SHIFT:
            if self.stats.game_active:
                self.stats.game_active = False
            elif self.stats.highscores_display:
                self.stats.highscores_display = False
        elif event.key == pg.K_BACKSPACE:
            self.nickname.user_text = self.nickname.user_text[:-1]
        elif event.key == pg.K_RETURN:
            self.nickname.save()
        else:
            self.nickname.user_text += event.unicode

    
    def check_button(self, mouse_x, mouse_y) -> None:
        """Start a new game when the player clicks Play.""" 
        play_clicked = self.start_page.start_btn.rect.collidepoint(mouse_x, mouse_y)
        highscores_clicked = self.start_page.highscore_btn.rect.collidepoint(mouse_x, mouse_y)
        if play_clicked and not self.stats.game_active:
            self.wait_nickname()
            self.build_game()
        elif highscores_clicked:
            self.stats.highscores_display = True


    def wait_nickname(self) -> None:
        """Display a text input and wait to a nickname."""
        while not self.nickname.has_value:
            self.settings.background()
            self.nickname.blit_me()
            self.check_events()
            pg.display.flip()


    def build_game(self) -> None:
        """Initialize all game elements."""
        self.settings.initialize_dynamic_settings()
        pg.mouse.set_visible(False)

        self.stats.reset_stats()
        self.stats.game_active = True

        self.scoreboard.prep_score()
        self.scoreboard.prep_high_score()
        self.scoreboard.prep_level()
        self.scoreboard.prep_ship()

        self.aliens.empty()
        self.bullets.empty()
        
        self.aliens.create_fleet()
        self.ship.center_ship()


    