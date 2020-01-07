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
	
	# def draw_edges(self, win, list_coordinators):
	# 	for coordinator in list_coordinators:
	# 		for y in range(9)
	# 			if coordinator
	# 			for x in range(9)

	def list_same_row(self, win):
		list_same_row = []
		group = []
		for y in range(9):
			for x in range(9):
				if(self.board[y][x] == 0): 
					coordinator = Coordinator(y, x, self.board[y][x])
					group.append(coordinator)
			list_same_row.append(group)
			group = []
		return list_same_row

	def draw_vertexes(self, win):
		list_coordinators = []
		for i in range(9):
			for j in range(9):
				if(self.board[i][j] == 0):
					x = j * 75 + 600
					y = i * 75 + 50
					current_coordinator = Coordinator(y, x, self.board[i][j])
					list_coordinators.append(current_coordinator)
					text_surf = FONT.render("["+ str(i) + ',' + str(j) + "]", True, (0,0,255))
					pygame.draw.circle(win, (220,220,220), (x, y), 30)
					win.blit(text_surf, (x,y))
		return list_coordinators

	def group_coordinator(self, board):
		min_x = 0
		group = []
		sudoku_group = []
		current_x = 0
		y = 0
		while(True):
			max_x = min_x + 3
			for x in range(min_x, max_x):
				group.append(self.board[y][x])
				current_x = x
				if (y + 1) % 3 == 0 and (x + 1) % 3 == 0:
					sudoku_group.append(group)
					group = []
			if y == 8 and x == 8:
				break
			elif (y + 1) % 3 == 0 and current_x == 8:
				y = y + 1
				min_x = 0
			elif (y + 1) % 3 == 0:
				y = y - 2
				min_x = current_x + 1
			else: y = y + 1
		return sudoku_group

	def draw_graph(self, win):
		arr = self.draw_vertexes(win)
		self.draw_line(win, arr)