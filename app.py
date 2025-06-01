import tkinter as tk
from sudoku_board import SudokuBoard
from menu import Menu

class SudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")

        # Create a frame for the Sudoku board
        self.board_frame = tk.Frame(root)
        self.board_frame.pack()

        # Initialize the Sudoku board
        self.sudoku_board = SudokuBoard(self.board_frame)

        # Create buttons for user interaction (e.g., check solution, clear board)
        self.check_button = tk.Button(root, text="Check", command=self.check_solution)
        self.check_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(root, text="Clear", command=self.sudoku_board.clear_board)
        self.clear_button.pack(side=tk.RIGHT)

        # Create the menu
        self.menu = Menu(self.root)

    def check_solution(self):
        if self.sudoku_board.is_valid():
            print("Correct!")
        else:
            print("Incorrect!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
