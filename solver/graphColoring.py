import pygame
import time

def graph_coloring_auto_play(board, win, play_time, strikes, button_list):
    win.redraw_window(play_time, strikes, button_list)
    pygame.display.update()