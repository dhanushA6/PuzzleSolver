import random

class Constant:
    UNASSIGNED = 0
    GRID_SIZE = 9
    BOX_SIZE = 3
    NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    LEVEL_NAME = [
        'Easy',
        'Medium',
        'Hard',
        'Very hard',
        'Insane',
        'Inhuman'
    ]
    LEVEL = [29, 38, 47, 56, 65, 74]

CONSTANT = Constant()

def newGrid(size):
    """
    Create a new grid with the given size.

    Args:
        size (int): Size of the grid.

    Returns:
        list: New grid.
    """
    arr = [[CONSTANT.UNASSIGNED for _ in range(size)] for _ in range(size)]
    for i in range(size * size):
        arr[i // size][i % size] = CONSTANT.UNASSIGNED
    return arr

def isColSafe(grid, col, value):
    """
    Check if it's safe to place a value in a column.

    Args:
        grid (list): Sudoku grid.
        col (int): Column index.
        value (int): Value to be placed.

    Returns:
        bool: True if it's safe to place the value, False otherwise.
    """
    for row in range(CONSTANT.GRID_SIZE):
        if grid[row][col] == value:
            return False
    return True

def isRowSafe(grid, row, value):
    """
    Check if it's safe to place a value in a row.

    Args:
        grid (list): Sudoku grid.
        row (int): Row index.
        value (int): Value to be placed.

    Returns:
        bool: True if it's safe to place the value, False otherwise.
    """
    for col in range(CONSTANT.GRID_SIZE):
        if grid[row][col] == value:
            return False
    return True

def isBoxSafe(grid, box_row, box_col, value):
    """
    Check if it's safe to place a value in a box.

    Args:
        grid (list): Sudoku grid.
        box_row (int): Row index of the box.
        box_col (int): Column index of the box.
        value (int): Value to be placed.

    Returns:
        bool: True if it's safe to place the value, False otherwise.
    """
    for row in range(CONSTANT.BOX_SIZE):
        for col in range(CONSTANT.BOX_SIZE):
            if grid[row + box_row][col + box_col] == value:
                return False
    return True

def isSafe(grid, row, col, value):
    """
    Check if it's safe to place a value in a given position.

    Args:
        grid (list): Sudoku grid.
        row (int): Row index.
        col (int): Column index.
        value (int): Value to be placed.

    Returns:
        bool: True if it's safe to place the value, False otherwise.
    """
    return (isColSafe(grid, col, value) and
            isRowSafe(grid, row, value) and
            isBoxSafe(grid, row - row % 3, col - col % 3, value) and
            value != CONSTANT.UNASSIGNED)

def findUnassignedPos(grid, pos):
    """
    Find an unassigned position in the grid.

    Args:
        grid (list): Sudoku grid.
        pos (dict): Dictionary to store the position.

    Returns:
        bool: True if an unassigned position is found, False otherwise.
    """
    for row in range(CONSTANT.GRID_SIZE):
        for col in range(CONSTANT.GRID_SIZE):
            if grid[row][col] == CONSTANT.UNASSIGNED:
                pos['row'] = row
                pos['col'] = col
                return True
    return False

def shuffleArray(arr):
    """
    Shuffle the elements of an array.

    Args:
        arr (list): Array to be shuffled.

    Returns:
        list: Shuffled array.
    """
    curr_index = len(arr)
    while curr_index != 0:
        rand_index = random.randint(0, curr_index - 1)
        curr_index -= 1
        temp = arr[curr_index]
        arr[curr_index] = arr[rand_index]
        arr[rand_index] = temp
    return arr

def isFullGrid(grid):
    """
    Check if the grid is full.

    Args:
        grid (list): Sudoku grid.

    Returns:
        bool: True if the grid is full, False otherwise.
    """
    return all(value != CONSTANT.UNASSIGNED for row in grid for value in row)

def sudokuCreate(grid):
    """
    Create a Sudoku grid.

    Args:
        grid (list): Sudoku grid.

    Returns:
        bool: True if the grid is successfully created, False otherwise.
    """
    unassigned_pos = {'row': -1, 'col': -1}
    if not findUnassignedPos(grid, unassigned_pos):
        return True
    number_list = shuffleArray(CONSTANT.NUMBERS.copy())
    row, col = unassigned_pos['row'], unassigned_pos['col']
    for num in number_list:
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            if isFullGrid(grid):
                return True
            elif sudokuCreate(grid):
                return True
            grid[row][col] = CONSTANT.UNASSIGNED
    return isFullGrid(grid)

def sudokuCheck(grid):
    """
    Check if a Sudoku grid is solvable.

    Args:
        grid (list): Sudoku grid.

    Returns:
        bool: True if the Sudoku grid is solvable, False otherwise.
    """
    unassigned_pos = {'row': -1, 'col': -1}
    if not findUnassignedPos(grid, unassigned_pos):
        return True
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            if isSafe(grid, i, j, num):
                if isFullGrid(grid):
                    return True
                elif sudokuCreate(grid):
                    return True
    return isFullGrid(grid)

def removeCells(grid, level):
    """
    Remove cells from the Sudoku grid to create a puzzle.

    Args:
        grid (list): Sudoku grid.
        level (int): Level of the puzzle.

    Returns:
        list: Sudoku grid with some cells removed.
    """
    res = [row[:] for row in grid]
    attempts = level
    while attempts > 0:
        row = rand()
        col = rand()
        while res[row][col] == 0:
            row = rand()
            col = rand()
        res[row][col] = CONSTANT.UNASSIGNED
        attempts -= 1
    return res

def sudokuGen(level):
    """
    Generate a Sudoku puzzle.

    Args:
        level (int): Level of the puzzle.

    Returns:
        dict: Dictionary containing the original Sudoku grid and the puzzle.
    """
    sudoku = newGrid(CONSTANT.GRID_SIZE)
    check = sudokuCreate(sudoku)
    if check:
        question = removeCells(sudoku, level)
        return {
            'original': sudoku,
            'question': question
        }
    return None

def rand():
    """
    Generate a random number within the range of GRID_SIZE.

    Returns:
        int: Random number.
    """
    return random.randint(0, CONSTANT.GRID_SIZE - 1)
