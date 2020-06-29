board1 = [
    [0, 0, 4, 8, 0, 6, 1, 0, 0],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 6, 0],
    [0, 1, 2, 0, 0, 0, 7, 5, 0],
    [0, 0, 6, 0, 0, 0, 2, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 1, 3, 0, 7, 8, 0, 0],
    [4, 0, 0, 9, 8, 5, 0, 0, 2],
    [0, 0, 0, 4, 0, 1, 0, 0, 0]
]

def solve_board(bo):
    """Solves the board recursively using the backtracking algorithm"""
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if validate_board(bo, i, (row, col)):
            bo[row][col] = i
            if solve_board(bo):
                return True
            bo[row][col] = 0
    return False


def validate_board(bo, num, pos):
    """Validates if the board breaks the Sudoku rules"""
    # Checks the columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Checks the rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Checks the 3x3 boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    """Prints the given board in the classic Sudoku format for a nice visual"""
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """Finds the position of the elements in the board which are empty (zero)"""
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


print("Here's the original board:")
time.sleep(0.5)
print_board(board1)
print("Solving.....")
time.sleep(2)
solve_board(board1)
print_board(board1)
print("Solved!")board1 = [
    [0, 0, 4, 8, 0, 6, 1, 0, 0],
    [0, 0, 0, 5, 0, 9, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 6, 0],
    [0, 1, 2, 0, 0, 0, 7, 5, 0],
    [0, 0, 6, 0, 0, 0, 2, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 1, 3, 0, 7, 8, 0, 0],
    [4, 0, 0, 9, 8, 5, 0, 0, 2],
    [0, 0, 0, 4, 0, 1, 0, 0, 0]
]

import time
def solve_board(bo):
    """Solves the board recursively using the backtracking algorithm"""
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if validate_board(bo, i, (row, col)):
            bo[row][col] = i
            if solve_board(bo):
                return True
            bo[row][col] = 0
    return False


def validate_board(bo, num, pos):
    """Validates if the board break the Sudoku rules"""
    # Checks the columns
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Checks the rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Checks the 3x3 boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def print_board(bo):
    """Prints the given board in the classic Sudoku format for a nice visual"""
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    """Finds the position of the elements in the board which are empty (zero)"""
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


print("Here's the original board:\n")

print_board(board1)
print("\n\n")

print("Solved!\n")
print_board(board1)

