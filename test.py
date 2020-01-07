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
    current_x = 0
    y = 0
    while(y < 8 or min_x < 8):
        print(y)
        max_x = min_x + 3
        for x in range(min_x, max_x):
            current_x = x
        # do something
        if (y + 1) % 3 == 0 and current_x == 8:
            y = y + 1
            min_x = 0
        elif (y + 1) % 3 == 0:
            y = y - 2
            min_x = current_x + 1
        else: y = y + 1

main()
