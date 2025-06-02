import random

class PlayerAI:
    def __init__(self, sudoku_board):
        self.sudoku_board = sudoku_board

    def make_move(self):
        empty_cells = [(r, c) for r in range(9) for c in range(9) if self.sudoku_board.board[r][c] == 0]
        if not empty_cells:
            return False  # No empty cells left to fill

        row, col = random.choice(empty_cells)
        possible_numbers = [num for num in range(1, 10) if self.sudoku_board.is_valid_move(num, row, col)]

        if possible_numbers:
            chosen_number = random.choice(possible_numbers)
            self.sudoku_board.board[row][col] = chosen_number
            return True
        else:
            return False

    def solve_puzzle(self):
        while self.make_move():
            pass  # Keep making moves until no more valid moves can be made
