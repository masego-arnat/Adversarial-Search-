def player(board):
    # Count the number of X's and O's to determine whose turn it is
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    return 'X' if x_count <= o_count else 'O'

def actions(board):
    # Return all possible moves (empty cells)
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]

def result(board, action):
    # Create a deep copy of the board and apply the move
    new_board = [row[:] for row in board]
    i, j = action
    if new_board[i][j] is not None:
        raise ValueError("Invalid action: cell is already occupied")
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def terminal(board):
    # Check if the game is over (win or draw)
    if winner(board) is not None:
        return True
    if all(board[i][j] is not None for i in range(3) for j in range(3)):
        return True
    return False

def utility(board):
    # Return the utility of a terminal board
    win = winner(board)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None

    current_player = player(board)
    if current_player == 'X':
        best_value = -float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = min_value(new_board)
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = max_value(new_board)
            if value < best_value:
                best_value = value
                best_move = action
        return best_move

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

# Example usage:
# board = [[None, None, None], [None, None, None], [None, None, None]]
# move = minimax(board)
# print(move)  # This will print the best move for the AI
