import pygame
import time

def graph_coloring_auto_play(board, win, play_time, strikes, button_list, graph):
    disable_graph = False
    win.redraw_window(play_time, strikes, button_list, disable_graph)
    pygame.display.update()
    solve(graph)

def solve(graph):
    list_resolved_coordinator = []
    list_coordinators = graph.list_coordinators
    same_row = graph.list_same_row()[0]
    same_col = graph.list_same_col()[0]
    same_group = graph.list_same_group()[0]
    values = [1,2,3,4,5,6,7,8,9]
    for coordinator in list_coordinators:
        if coordinator.value == 0:
            valid_values = values
            if is_resolved(coordinator, list_resolved_coordinator):
                continue
            add_value(coordinator, list_resolved_coordinator, valid_values)
            x = coordinator.x_board
            y = coordinator.y_board
            for row in same_row[x]:
                if is_resolved(row, list_resolved_coordinator):
                    continue
                valid_values = values
                add_value(row, list_resolved_coordinator, valid_values)
            for col in same_col[y]:
                if is_resolved(col, list_resolved_coordinator):
                    continue
                valid_values = values
                add_value(col, list_resolved_coordinator, valid_values)
            for group in same_group[detect_group_number(coordinator, same_group)]:
                if is_resolved(group, list_resolved_coordinator):
                    continue
                valid_values = values
                add_value(group, list_resolved_coordinator, valid_values)

def is_resolved(current_coordinator, list_resolved_coordinator):
    for coordinator in list_resolved_coordinator:
        if current_coordinator.x_board == coordinator.x_board and current_coordinator.y_board == coordinator.y_board:
            return True
    return False

def detect_group_number(coordinator, same_group):
    number = 0
    for i in range(same_group.__len__() - 1):
        for j in range(same_group[i].__len__() - 1):
            if coordinator.x_board == same_group[i][j].x_board and coordinator.y_board == same_group[i][j].y_board:
                return i
    return number

def is_valid_value(x, y , value):
    # do something
    return True



def add_value(coordinator, list_resolved_coordinator, valid_values):
    current_value = 0
    for value in valid_values:
        if is_valid_value:
            current_value = value
            coordinator.value = value
            list_resolved_coordinator.append(coordinator)
            break
    if current_value:
        valid_values.remove(current_value)