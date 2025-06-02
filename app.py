import tkinter as tk
from sudoku_board import SudokuBoard
from player_ai import PlayerAI

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hey there! Welcome to Sudoku")

        # Create a frame for the Sudoku board
        self.board_frame = tk.Frame(root)
        self.board_frame.pack()

        # Initialize the Sudoku board
        self.sudoku_board = SudokuBoard(self.board_frame)

        # Initialize PlayerAI with the Sudoku board
        self.player_ai = PlayerAI(self.sudoku_board)

        # Create buttons for user interaction (e.g., check solution, clear board)
        self.check_button = tk.Button(root, text="Check", command=self.check_solution)
        self.check_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(root, text="Clear", command=self.sudoku_board.clear_board)
        self.clear_button.pack(side=tk.RIGHT)

        # Create a button to let the AI solve the puzzle
        self.ai_solve_button = tk.Button(root, text="AI Solve", command=self.ai_solve_puzzle)
        self.ai_solve_button.pack()

    def check_solution(self):
        if self.sudoku_board.check_solution():
            print("Congratulations! You solved it!")
        else:
            print("Incorrect solution. Try again.")

    def ai_solve_puzzle(self):
        self.player_ai.solve_puzzle()
        # Update the board display after AI solves
        self.sudoku_board.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
