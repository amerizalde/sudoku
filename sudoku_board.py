import tkinter as tk
import random

class SudokuBoard:
    def __init__(self, parent):
        self.parent = parent
        self.board = self.generate_sudoku()
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_board()

    def generate_sudoku(self):
        # Generate a valid Sudoku puzzle using backtracking algorithm
        board = [[0 for _ in range(9)] for _ in range(9)]
        if not self.solve_sudoku(board, 0, 0):
            raise Exception("Failed to generate a valid Sudoku puzzle")
        self.remove_numbers(board)
        return board

    def solve_sudoku(self, board, row, col):
        if row == 8 and col == 9:
            return True
        if col == 9:
            row += 1
            col = 0
        if board[row][col] != 0:
            return self.solve_sudoku(board, row, col + 1)
        for num in range(1, 10):
            if self.is_valid_move(num, row, col, board):
                board[row][col] = num
                if self.solve_sudoku(board, row, col + 1):
                    return True
                board[row][col] = 0
        return False

    def remove_numbers(self, board):
        # Remove numbers to create the final puzzle
        count = random.randint(40, 50)
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
                if not self.is_valid_move(int(self.cells[i][j].get()), i, j, self.board):
                    return False
        return True

    def is_valid_move(self, num, row, col, board=None):
        # Check row and column
        if board is None:
            for i in range(9):
                if self.cells[row][i] == str(num) or self.cells[i][col] == str(num):
                    return False
        else:
            for i in range(9):
                if board[row][i] == num or board[i][col] == num:
                    return False
        # Check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        if board is None:
            for i in range(3):
                for j in range(3):
                    if self.cells[start_row + i][start_col + j] == str(num):
                        return False
        else:
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
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
