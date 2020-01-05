# pylint: disable=no-member
import pygame
import time
from solver.backtracking import solve, valid, back_tracking_auto_play
from component.grid import Grid
from component.cube import Cube
from component.button import Button
from component.screen import Screen
pygame.font.init()

def main():
    board = Grid(9, 9, 500, 500)
    win = Screen(540, 600, board)
    button1 = Button(win, 0, 502, 100, 50, 'Back Tracking', back_tracking_auto_play)
    button_list = [button1]
    key = None
    run = True
    start = time.time()
    strikes = 0
    while run:
        play_time = round(time.time() - start)
        # auto_play(board, win, play_time, strikes)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.place(board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                            strikes += 1
                        key = None
                        if board.is_finished():
                            print("Game over")
                            run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if event.button == 1:
                    for button in button_list:
                        if button.rect.collidepoint(event.pos):
                            button.callback(board, win, play_time, strikes, button_list)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key != None:
            board.sketch(key)
        
        win.redraw_window(play_time, strikes, button_list)
        pygame.display.update()


main()
pygame.quit()