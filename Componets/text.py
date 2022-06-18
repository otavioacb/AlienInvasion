import pygame as pg

class Text:
    """
        This class represent a text component.
    """

    def __init__(self, screen, text, pos) -> None:
        """Initialize text parameters."""
        self.screen = screen 
        self.text = text.encode("utf-8")
        self.pos_x, self.pos_y = pos

        self.text_color = (255, 255, 255)
        self.text_font = pg.font.Font(None, 50)
        self.text_rect = pg.Rect(self.pos_x, self.pos_y, 100, 40)

    
    def blit_text(self) -> None:
        """Display text."""
        render_text = self.text_font.render(self.text, True, self.text_color)
        self.screen.blit(render_text, self.text_rect)
