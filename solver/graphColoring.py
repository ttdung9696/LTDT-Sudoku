import pygame
import time

def graph_coloring_auto_play(board, win, play_time, strikes, button_list, graph):
    disable_graph = False
    win.redraw_window(play_time, strikes, button_list, disable_graph)
    pygame.display.update()

def count_relation_vertex(graph):
