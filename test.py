def main():
    sudoku = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    min_x = 0
    min_y = 0
    max_y = 3
    for y in range(min_y, max_y):
        print(min_y)
        print(max_y)
        max_x = min_x + 3
        for x in range(min_x, max_x):
            print('y---x', y, x, sudoku[y][x])
            if x == max_x - 1 and min_y == max_y - 1:
                min_x = max_x
        if min_x < 9 and (y + 1) % 3 == 0:
            print('here 1')
            min_y = y - 2
            max_y = min_y + 3
        if min_x == 8 and (y + 1) % 3 == 0:
            print('here 2')
            min_y = y + 1
            max_y = min_y + 3
            min_x = 0
        if min_x == 8 and min_y == 8:
            print('here 3')
            break


main()