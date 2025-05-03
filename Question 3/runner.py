# from tictactoe import player, actions, result, winner, terminal, utility, minimax

# def display_board(board):
#     # Display the Tic-Tac-Toe board in the terminal
#     for row in board:
#         print(" | ".join([cell if cell is not None else " " for cell in row]))
#         print("-" * 5)

# def human_move(board):
#     # Allow the human player to make a move
#     while True:
#         try:
#             row = int(input("Enter the row (0, 1, 2): "))
#             col = int(input("Enter the column (0, 1, 2): "))
#             if (row, col) in actions(board):
#                 return (row, col)
#             else:
#                 print("Invalid move. Try again.")
#         except ValueError:
#             print("Invalid input. Please enter numbers.")

# def play_game():
#     # Initialize the board
#     board = [[None, None, None], [None, None, None], [None, None, None]]
#     print("Welcome to Tic-Tac-Toe!")
#     display_board(board)

#     while not terminal(board):
#         # Human player's turn
#         if player(board) == 'O':
#             print("\nYour turn (O):")
#             move = human_move(board)
#         else:
#             # AI's turn
#             print("\nAI's turn (X):")
#             move = minimax(board)
        
#         board = result(board, move)
#         display_board(board)

#     # Game over, display the result
#     if winner(board) == 'X':
#         print("AI wins!")
#     elif winner(board) == 'O':
#         print("You win!")
#     else:
#         print("It's a tie!")

# if __name__ == "__main__":
#     play_game() 