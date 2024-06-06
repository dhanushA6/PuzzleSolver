from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the homepage.

    Returns:
        Rendered HTML template (home.html)
    """
    return render_template('home.html')

@app.route('/sudoku_game', methods=['POST'])
def sudoku_game():
    """
    Render the Sudoku game page.

    Returns:
        Rendered HTML template (sudoku.html)
    """
    return render_template('sudoku.html')

@app.route('/wordsearch_game', methods=['POST'])
def wordsearch_game():
    """
    Render the Word Search game page.

    Returns:
        Rendered HTML template (wordsearch.html)
    """
    return render_template('wordsearch.html')


def is_valid(board, row, col, c):
    """
    Check if the attempted move is valid.

    Args:
        board (list): 2D list representing the Sudoku board.
        row (int): Row index of the cell.
        col (int): Column index of the cell.
        c (int): The number to be placed.

    Returns:
        bool: True if the move is valid, False otherwise.
    """

    # Dynamic Programming 
    # Memoization Concept 

    # It Reduces Time Complexity from O(2^n) to O(n) 
    # Space Complexity for memo(memory for DP) -O(n^2) 

    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
            return False
    return True


def solve_sudoku(board, memo={}):
    """
    Solve the Sudoku using backtracking algorithm.

    Args:
        board (list): 2D list representing the Sudoku board.
        memo (dict): Dictionary to store the intermediate states.

    Returns:
        list: Solved Sudoku board.
    """
    key = str(board)
    if key in memo:
        return memo[key]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for c in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    if is_valid(board, i, j, c):
                        board[i][j] = c
                        if solve_sudoku(board, memo):
                            memo[key] = board
                            return board
                        else:
                            board[i][j] = 0
                memo[key] = False
                return False
    memo[key] = board
    return board 




@app.route('/solve_sudoku', methods=['POST'])
def solve_sudoku_route():
    """
    Solve the provided Sudoku grid.

    Returns:
        JSON: Solved Sudoku grid.
    """
    data = request.json
    sudoku_grid = data['sudoku']
    solved_sudoku = solve_sudoku(sudoku_grid, {})
    return jsonify({'solved_sudoku': solved_sudoku}) 


if __name__ == '__main__':
    app.run(debug=True)
