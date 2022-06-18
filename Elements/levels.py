import pygame.font
import pygame as pg

class Levels:
    """
        This class represent the level text
        displayed in leves transition.
    """
    
    def __init__(self, ai_settings, screen, stats) -> None:
        self.settings = ai_settings
        self.stats = stats
        self.screen = screen

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 60)


    def show_level(self) -> None:
        """
            Display the current level.
        """
        level = self.stats.level
        level_str = f"Next level: {level}"

        self.level_image = self.font.render(level_str, True, self.text_color)
        
        x_pos = (self.settings.dimensions[0] - self.level_image.get_size()[0])/2
        y_pos = (self.settings.dimensions[1] - self.level_image.get_size()[1])/2

        self.screen.blit(self.level_image, dest=(x_pos, y_pos))
        pg.display.flip()