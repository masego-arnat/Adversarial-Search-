import tkinter as tk
from tkinter import messagebox
from tictactoe import player, actions, result, winner, terminal, utility, minimax

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        # Create a 3x3 grid of buttons
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 20),
                    width=5,
                    height=2,
                    command=lambda i=i, j=j: self.on_button_click(i, j),
                )
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_button_click(self, i, j):
        # Handle human player's move
        if self.board[i][j] is None and not terminal(self.board):
            self.board[i][j] = 'O'
            self.buttons[i][j].config(text='O')
            if terminal(self.board):
                self.end_game()
            else:
                # AI's move
                self.ai_move()

    def ai_move(self):
        # AI makes a move using the Minimax algorithm
        move = minimax(self.board)
        if move:
            i, j = move
            self.board[i][j] = 'X'
            self.buttons[i][j].config(text='X')
            if terminal(self.board):
                self.end_game()

    def end_game(self):
        # Display the result of the game
        win = winner(self.board)
        if win == 'X':
            messagebox.showinfo("Game Over", "AI wins!")
        elif win == 'O':
            messagebox.showinfo("Game Over", "You win!")
        else:
            messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_game()

    def reset_game(self):
        # Reset the board for a new game
        self.board = [[None, None, None], [None, None, None], [None, None, None]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop() 