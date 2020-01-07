import pygame
import time

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    print('checkbox', box_x, box_y)
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def back_tracking_auto_play(board, win, play_time, strikes, button_list):
    for i in range(9):
        for j in range(9):
            time.sleep(0.1)
            board.select(i, j)
            if board.cubes[i][j].value == 0:
                for rs in range(9):
                    board.sketch(rs + 1)
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            if board.is_finished():
                                win.redraw_window(play_time, strikes, button_list)
                                pygame.display.update()
                                print("Game over")
                                while True:
                                    True
                                    # run = False
            win.redraw_window(play_time, strikes, button_list)
            pygame.display.update()