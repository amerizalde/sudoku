import tkinter as tk
import random

class SudokuBoard:
    def __init__(self, parent):
        self.parent = parent
        self.board = self.generate_sudoku()
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_board()

    def generate_sudoku(self):
        # Generate a valid Sudoku puzzle (simplified version)
        board = [[0 for _ in range(9)] for _ in range(9)]
        numbers = list(range(1, 10))
        for i in range(9):
            random.shuffle(numbers)
            for j in range(9):
                if i % 3 == 0 and j % 3 == 0:
                    random.shuffle(numbers)
                board[i][j] = numbers[j]
        self.remove_numbers(board, 40)
        return board

    def remove_numbers(self, board, count):
        while count > 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if board[i][j] != 0:
                board[i][j] = 0
                count -= 1

    def create_board(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.board[i][j]
                cell_frame = tk.Frame(self.parent, bd=2, relief="sunken")
                cell_frame.grid(row=i, column=j)
                if cell_value != 0:
                    label = tk.Label(cell_frame, text=str(cell_value), font=("Helvetica", 16))
                    label.pack()
                else:
                    entry = tk.Entry(cell_frame, width=2, font=("Helvetica", 16), justify="center")
                    entry.bind("<KeyRelease>", lambda e, row=i, col=j: self.validate_input(e, row, col))
                    entry.pack()
                    self.cells[i][j] = entry

    def validate_input(self, event, row, col):
        value = event.widget.get()
        if not value.isdigit() or int(value) < 1 or int(value) > 9:
            event.widget.delete(0, tk.END)
            return
        self.cells[row][col] = value

    def check_solution(self):
        for i in range(9):
            for j in range(9):
                if not self.is_valid_move(int(self.cells[i][j].get()), i, j):
                    return False
        return True

    def is_valid_move(self, num, row, col):
        # Check row and column
        for i in range(9):
            if self.cells[row][i] == str(num) or self.cells[i][col] == str(num):
                return False
        # Check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.cells[start_row + i][start_col + j] == str(num):
                    return False
        return True

    def get_board(self):
        board = []
        for row in self.cells:
            board.append([int(cell.get()) if cell else 0 for cell in row])
        return board

    def clear_board(self):
        for i in range(9):
            for j in range(9):
                if isinstance(self.cells[i][j], tk.Entry):
                    self.cells[i][j].delete(0, tk.END)
