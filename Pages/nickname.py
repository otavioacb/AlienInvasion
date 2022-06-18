import pygame as pg

class Nickname:
    """
        This class represent a 
        text input to nickname user.
    """

    def __init__(self, screen, stats) -> None:
        self.screen = screen
        self.stats = stats
        self.has_value = False

        self.text_font = pg.font.Font(None, 32)
        self.title_font = pg.font.Font(None, 40)
        self.user_text = ""

        self.text_rect = pg.Rect(500, 260, 200, 32)
        self.color_rect = pg.Color("lightskyblue3")


    def title(self) -> None:
        """Display a label to nickname input."""
        title = "Your nickname:"
        title_rendered = self.title_font.render(title, True, (255, 255, 255))
        
        self.screen.blit(title_rendered, (500, 230))


    def blit_me(self) -> None:
        """Displaye nickname label and input."""
        pg.draw.rect(self.screen, self.color_rect, self.text_rect)

        text = self.text_font.render(self.user_text, True, (255, 255, 255))
        self.title()
        self.screen.blit(text, self.text_rect)


    def save(self) -> None:
        """Save the nickname at game stats."""
        self.stats.nickname = self.user_text
        self.has_value = True