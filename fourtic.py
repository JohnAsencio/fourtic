def evaluate_position(board):
    # Define the winning rows, columns, and diagonals
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(1, 0), (1, 1), (1, 2), (1, 3)],
        [(2, 0), (2, 1), (2, 2), (2, 3)],
        [(3, 0), (3, 1), (3, 2), (3, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1)],
        [(0, 2), (1, 2), (2, 2), (3, 2)],
        [(0, 3), (1, 3), (2, 3), (3, 3)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 3), (1, 2), (2, 1), (3, 0)]
    ]

    def check_winner(symbol):
        for combination in winning_combinations:
            if all(board[row][col] == symbol for row, col in combination):
                return True
        return False

    def count_symbols(symbol):
        return sum(row.count(symbol) for row in board)

    # Check if X has won
    if check_winner('X'):
        return 100

    # Check if O has won
    if check_winner('O'):
        return -100

    # If the board is full, it's a draw
    if count_symbols('.') == 0:
        return 0

    # Calculate the value for the side on move
    side_on_move = 'X' if count_symbols('X') == count_symbols('O') else 'O'

    return count_symbols(side_on_move) - count_symbols('O')

def negamax(board):
    def generate_moves(board):
        moves = []
        for i in range(4):
            for j in range(4):
                if board[i][j] == '.':
                    moves.append((i, j))
        return moves

    def make_move(board, move, symbol):
        i, j = move
        board[i][j] = symbol

    def undo_move(board, move):
        i, j = move
        board[i][j] = '.'

    def negamax_search(board, depth, symbol):
        if depth == 0 or evaluate_position(board) != 0:
            return evaluate_position(board)

        best_value = -float('inf')
        for move in generate_moves(board):
            make_move(board, move, symbol)
            value = -negamax_search(board, depth - 1, 'X' if symbol == 'O' else 'O')
            undo_move(board, move)
            best_value = max(best_value, value)

        return best_value

    best_value = -float('inf')
    best_move = None
    side_on_move = 'X' if count_symbols('X') == count_symbols('O') else 'O'

    for move in generate_moves(board):
        make_move(board, move, side_on_move)
        value = -negamax_search(board, float('inf'), side_on_move)
        undo_move(board, move)

        if value > best_value:
            best_value = value
            best_move = move

    return best_move

def read_position(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        return [list(line) for line in lines]

def print_result(side, value):
    print(f"{side} {value}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("input file not found")
        sys.exit(1)

    input_file = sys.argv[1]
    position = read_position(input_file)
    best_move = negamax(position)
    value = evaluate_position(position)
    side_on_move = 'X' if value > 0 else 'O'

    print_result(side_on_move, value)
