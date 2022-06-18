import pygame as pg
import pygame.font
from Componets.button import Button

class StartPage:

    
    def __init__(self, ai_settings, screen, highscores_db) -> None:
        """Initialize page details."""
        self.settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (255, 255, 255)
        self.font_title = pygame.font.SysFont(None, 100, italic=True)
        self.font_hg = pygame.font.SysFont(None, 40)
        self.font_copy_text = pygame.font.SysFont(None, 25)

        self.highscore_db = highscores_db


    def draw_details(self) -> None:
        """Create buttons and titles""" 
        self.title_text()
        self.copy_text()

        self.screen.blit(self.game_title_image, dest = self.title_pos)
        self.screen.blit(self.game_copy_image, dest = self.copy_pos)

        self.start_button()
        self.highscore_button()

    
    def draw_highscores(self) -> None:
        """Get 5 top highscores and draw."""
        highscores = self.highscore_db.get()
        x_pos = 100
        y_pos = 100
        for highscore in highscores:
            nickname = self.font_hg.render(highscore[0], True, self.text_color)
            score = self.font_hg.render(highscore[1], True, self.text_color)
            date = self.font_hg.render(highscore[2], True, self.text_color)

            self.screen.blit(nickname, dest=((x_pos+10), y_pos))
            self.screen.blit(score, dest=((x_pos+20), y_pos))
            self.screen.blit(date, dest=((x_pos+30), y_pos))

            y_pos += 30

        pg.display.flip()


    def title_text(self) -> None:
        """Display game title."""
        game_title_str = "Alien Invasion" 
        self.game_title_image = self.font_title.render(game_title_str, True, self.text_color)
        x_pos = (self.settings.dimensions[0] - self.game_title_image.get_size()[0]) / 2
        self.title_pos = (x_pos, 100)

    
    def start_button(self) -> None:
        """Display play button."""
        self.start_btn = Button(self.settings, self.screen, "Start", self.text_color, (530, 250))
        self.start_btn.draw()


    def highscore_button(self) -> None:
        """Display highscore button."""
        self.highscore_btn = Button(self.settings, self.screen, "Highscore", self.text_color, (480, 320))
        self.highscore_btn.draw()


    def copy_text(self) -> None:
        """Display copyright text."""
        game_copy_str = "@otavioacb - 2022"
        self.game_copy_image = self.font_copy_text.render(game_copy_str, True, self.text_color)
        x_pos = (self.settings.dimensions[0] - self.game_copy_image.get_size()[0]) / 2
        y_pos = self.settings.dimensions[1] - 30
        self.copy_pos = (x_pos, y_pos)

    
    def display(self) -> None:
        """Change display elements."""
        self.settings.background()
        self.draw_details()
        pg.mouse.set_visible(True)
        pg.display.flip()
