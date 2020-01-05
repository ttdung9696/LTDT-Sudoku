# pylint: disable=no-member
import pygame

class Screen:
    def __init__(self, x, y, board):
        self.win = pygame.display.set_mode((x, y))
        pygame.display.set_caption("Sudoku")
        self.board = board

    def format_time(self ,secs):
        sec = secs%60
        minute = secs//60
        hour = minute//60

        mat = " " + str(minute) + ":" + str(sec)
        return mat


    def redraw_window(self, time, strikes, button_list):
        self.win.fill((255,255,255))
        for button in button_list:
            button.draw_button(self.win)
        # Draw time
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("Time: " + self.format_time(time), 1, (0,0,0))
        self.win.blit(text, (540 - 160, 560))
        # Draw Strikes
        text = fnt.render("X " * strikes, 1, (255, 0, 0))
        self.win.blit(text, (20, 560))
        # Draw grid and board
        self.board.draw(self.win)

