from Componets.text import Text

class HighscorePage:
    """
        Set up highscore page funtions.
    """

    def __init__(self, screen, settings, highscore_db) -> None:
        self.screen = screen
        self.settings = settings
        self.highscore_db = highscore_db


    def draw_highscores(self) -> None:
        """Display the 5 best highscores."""
        init_x = 400
        init_y = 200
        highscores = self.highscore_db.get()
        self.settings.background()
        self.draw_highscore_title()
        for highscore in highscores:
            user, score, date = highscore

            user_txt = Text(self.screen, user, (init_x, init_y))
            score_txt = Text(self.screen, str(score), (init_x+150, init_y))
            date_txt = Text(self.screen, date, (init_x+250, init_y))
            
            user_txt.blit_text()
            score_txt.blit_text()
            date_txt.blit_text()

            init_y += 50

    
    def draw_highscore_title(self) -> None:
        """Draw a highscore title."""
        pos = (510, 150)
        highscore_title = Text(self.screen, "Highscores", pos)
        highscore_title.blit_text()