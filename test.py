# def list_same_rows():
#     sudoku = [
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
#     ]
#     list_same_row = []
#     group = []
#     for y in range(9):
#         for x in range(9):
#             if(sudoku[y][x] == 0):
#                 group.append(str(y) + ' , ' + str(x))
#         list_same_row.append(group)
#         group = []
#     return list_same_row

# def list_same_cols():
#     sudoku = [
#         [7, 8, 0, 4, 0, 0, 1, 2, 0],
#         [6, 0, 0, 0, 7, 5, 0, 0, 9],
#         [0, 0, 0, 6, 0, 1, 0, 7, 8],
#         [0, 0, 7, 0, 4, 0, 2, 6, 0],
#         [0, 0, 1, 0, 5, 0, 9, 3, 0],
#         [9, 0, 4, 0, 6, 0, 0, 0, 5],
#         [0, 7, 0, 3, 0, 0, 0, 1, 2],
#         [1, 2, 0, 0, 0, 7, 4, 0, 0],
#         [0, 4, 9, 2, 0, 6, 0, 0, 7]
#     ]
#     list_same_cols = []
#     group = []
#     for x in range(9):
#         for y in range(9):
#             if(sudoku[y][x] == 0):
#                 group.append(str(y) + ' , ' + str(x) )
#         list_same_cols.append(group)
#         group = []
#     return list_same_cols

# # print(list_same_rows())
# print(list_same_cols())

def list_same_row(self, list_coordinators):
    list_same_row = []
    group = []
    for y in range(9):
        for x in range(9):
            for coordinator in list_coordinators:
                if coordinator.x == x and coordinator.y == y and coordinator.value == 0:
                    group.append(coordinator)
        list_same_row.append(group)
        group = []
    return list_same_row
