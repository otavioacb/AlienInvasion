from Database.highscores import Highscores

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings) -> None:
        """Initialize statistics."""
        self.ai_settings = ai_settings

        self.game_active = False
        self.highscores_display = False
        self.high_score = 0
        self.nickname = "user1"

        self.high_score_db = Highscores()

        self.reset_stats()


    def add_scoreboard(self, scoreboard) -> None:
        """Get scoreboard instance."""
        self.scoreboard = scoreboard


    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit 
        self.score = 0
        self.level = 1

    
    def check_high_score(self) -> None:
        """Check to see if there's a new high score."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.scoreboard.prep_high_score()