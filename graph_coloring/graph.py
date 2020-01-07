# pylint: disable=no-member
import pygame
import time
from turtle import Turtle, Screen
from random import randint	
from graph_coloring.coordinator import Coordinator
pygame.init()
FONT = pygame.font.Font(None, 20)

class Graph:

	def __init__(self, board):
		self.board = board

	def draw_line(self, win, list_coordinators):
		i = 0
		while i <= len(list_coordinators) - 2:
			time.sleep(0.2)
			pygame.draw.line(win, (255,0,255), (list_coordinators[i].x, list_coordinators[i].y), (list_coordinators[i + 1].x, list_coordinators[i + 1].y), 2)
			pygame.display.update()
			i=i+1

	def draw_circle(self, win, list_coordinators):
		for i in range(9):
			for j in range(9):
				if(self.board[i][j] == 0):
					x = j * 75 + 600
					y = i * 75 + 50
					current_coordinator = Coordinator(x, y)
					list_coordinators.append(current_coordinator)
					text_surf = FONT.render("["+ str(i) + ',' + str(j) + "]", True, (0,0,255))
					pygame.draw.circle(win, (220,220,220), (x, y), 30)
					win.blit(text_surf, (x,y))
					# pygame.display.update()

	def draw_graph(self, win):
		list_coordinators = []
		self.draw_circle(win, list_coordinators)
		self.draw_line(win, list_coordinators)