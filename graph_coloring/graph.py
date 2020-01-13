# pylint: disable=no-member
import pygame
import time
from random import randint
from graph_coloring.coordinator import Coordinator
pygame.init()
FONT = pygame.font.Font(None, 20)


class Graph:

    def __init__(self, board):
        self.board = board
        self.list_coordinators = []


    def draw_edges(self, win):
        same_row = self.list_same_row()[1]
        same_col = self.list_same_col()[1]
        same_group = self.list_same_group()[1]
        for row in same_group:
            for i in range(row.__len__() - 1):
                # time.sleep(0.2)
                pygame.draw.line(
                    win, (255, 0, 255), (row[i].x_draw, row[i].y_draw), (row[i + 1].x_draw, row[i + 1].y_draw), 2)
                pygame.display.update()
        for col in same_col:
            for i in range(col.__len__() - 1):
                # time.sleep(0.2)
                pygame.draw.line(
                    win, (255, 0, 255), (col[i].x_draw, col[i].y_draw), (col[i + 1].x_draw, col[i + 1].y_draw), 2)
                pygame.display.update()
        for row in same_row:
            for i in range(row.__len__() - 1):
                # time.sleep(0.2)
                pygame.draw.line(
                    win, (255, 0, 255), (row[i].x_draw, row[i].y_draw), (row[i + 1].x_draw, row[i + 1].y_draw), 2)
                pygame.display.update()


    def list_same_row(self):
        list_same_row = []
        list_unresolved_same_row = []
        group = []
        unresolved_group = []
        for x in range(9):
            for coordinator in self.list_coordinators:
                if coordinator.x_board == x:
                    group.append(coordinator)
                if coordinator.x_board == x and coordinator.value == 0:
                    unresolved_group.append(coordinator)
            list_same_row.append(group)
            list_unresolved_same_row.append(unresolved_group)
            group = []
            unresolved_group = []
        return [list_same_row, list_unresolved_same_row]

    def list_same_col(self):
        list_same_col = []
        list_unresolved_same_col = []
        unresolved_group = []
        group = []
        for y in range(9):
            for coordinator in self.list_coordinators:
                if coordinator.y_board == y:
                    group.append(coordinator)
                if coordinator.y_board == y and coordinator.value == 0:
                    unresolved_group.append(coordinator)
            list_same_col.append(group)
            list_unresolved_same_col.append(unresolved_group)
            group = []
            unresolved_group = []
        return [list_same_col, list_unresolved_same_col]


    def list_same_group(self):
        min_x = 0
        group = []
        list_unresolved_same_group = []
        unresolved_group = []
        sudoku_group = []
        current_x = 0
        y = 0
        while(True):
            max_x = min_x + 3
            for x in range(min_x, max_x):
                for coordinator in self.list_coordinators:
                    if coordinator.x_board == x and coordinator.y_board == y:
                        group.append(coordinator)
                    if coordinator.x_board == x and coordinator.y_board == y and coordinator.value == 0:
                        unresolved_group.append(coordinator)
                if (y + 1) % 3 == 0 and (x + 1) % 3 == 0:
                    list_unresolved_same_group.append(unresolved_group)
                    sudoku_group.append(group)
                    group = []
                    unresolved_group = []
                current_x = x
            if y == 8 and x == 8:
                break
            elif (y + 1) % 3 == 0 and current_x == 8:
                y = y + 1
                min_x = 0
            elif (y + 1) % 3 == 0:
                y = y - 2
                min_x = current_x + 1
            else:
                y = y + 1
        return [sudoku_group, list_unresolved_same_group]

    def draw_vertexes(self, win):
        list_coordinators = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    x_draw = 0
                    y_draw = 0
                    current_coordinator = Coordinator(i ,j ,x_draw, y_draw, self.board[i][j])
                    list_coordinators.append(current_coordinator)
                elif self.board[i][j] == 0:
                    x_draw = j * 75 + 600
                    y_draw = i * 75 + 50
                    current_coordinator = Coordinator(i ,j ,x_draw, y_draw, self.board[i][j])
                    list_coordinators.append(current_coordinator)
                    text_surf = FONT.render(
                        "[" + str(i) + ',' + str(j) + "]", True, (0, 0, 255))
                    pygame.draw.circle(win, (220, 220, 220), (x_draw, y_draw), 30)
                    win.blit(text_surf, (x_draw, y_draw))
        return list_coordinators
    
    def draw_graph(self, win):
        self.list_coordinators = self.draw_vertexes(win)
        self.draw_edges(win)
