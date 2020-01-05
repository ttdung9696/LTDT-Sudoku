# pylint: disable=no-member
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (13, 255, 0)
YELLOW = (0, 255, 20)
BRIGHT_YELLOW = (255, 255, 20)
FONT = pygame.font.Font(None, 20)
INACTIVE_COLOR = pygame.Color('dodgerblue4')

class Button:
    def __init__(self, win, x, y, width, height, text, callback):
        text_surf = FONT.render(text, True, WHITE)
        button_rect = pygame.Rect(x, y, width, height)
        text_rect = text_surf.get_rect(center=button_rect.center)
        self.rect = button_rect
        self.text = text_surf
        self.text_rect = text_rect
        self.color = INACTIVE_COLOR
        self.callback = callback

    def draw_button(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, self.text_rect)