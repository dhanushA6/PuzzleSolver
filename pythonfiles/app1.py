from flask import Flask, request, jsonify , render_template
import json 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/sudoku_game', methods = ['POST'])
def sudoku_game(): 
    return render_template('sudoku.html')

@app.route('/wordsearch_game', methods = ['POST'])
def wordsearch_game(): 
    return render_template('wordsearch.html')


def is_valid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c:
            return False
        if board[row][i] == c:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
            return False
    return True


def solve_sudoku_(board, memo={}):
    key = str(board)
    if key in memo:
        return memo[key]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                for c in [1, 2, 3, 4, 5, 6, 7,8, 9]:
                    if is_valid(board, i, j, c):
                        board[i][j] = c
                        if solve_sudoku_(board, memo):  # Change the recursive call to solve_sudoku_
                            memo[key] = board  # Store the result in memo
                            return board  # Return the board when solution found
                        else:
                            board[i][j] = 0
                memo[key] = False  # Store False in memo for invalid states
                return False
    memo[key] = board  # Store the solved board in memo
    return board  # Return the board when all cells are filled





@app.route('/solve_sudoku', methods=['POST'])
def solve_sudoku():
    data = request.json  # Get JSON data from the request
    sudoku_grid = data['sudoku']  # Extract the sudoku grid
    # Solve the Sudoku
    solved_sudoku = solve_sudoku_(sudoku_grid, {})
    # Return the solved Sudoku as JSON
    return jsonify({'solved_sudoku': solved_sudoku}) 




if __name__ == '__main__':
    app.run(debug=True)