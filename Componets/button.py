import pygame.font

class Button:

    def __init__(self, ai_settings, screen, msg, txt_color, pos, bg_color=None) -> None:
        """Initialize button attributes."""
        self.screen = screen

        self.width, self.height = 200, 50
        self.button_x, self.button_y = pos
        self.button_color = bg_color  
        self.text_color = txt_color
        self.font = pygame.font.SysFont(None, 70)

        self.rect = pygame.Rect(self.button_x, self.button_y, self.width, self.height)

        self.prep_msg(msg)

    
    def prep_msg(self, msg) -> None:
        """Turn message into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw(self) -> None:
        """Draw blank button and then draw message."""
        self.screen.blit(self.msg_image, self.rect)