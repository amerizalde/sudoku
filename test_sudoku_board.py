import unittest
from sudoku_board import SudokuBoard

class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.sudoku_board = SudokuBoard(None)

    def test_no_duplicates_in_rows(self):
        board = self.sudoku_board.board
        for row in board:
            unique_nums = [num for num in row if num != 0]
            self.assertEqual(len(set(unique_nums)), len(unique_nums), f"Duplicates found in row: {row}")

    def test_no_duplicates_in_columns(self):
        board = self.sudoku_board.board
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            unique_nums = [num for num in column if num != 0]
            self.assertEqual(len(set(unique_nums)), len(unique_nums), f"Duplicates found in column: {column}")

    def test_valid_puzzle(self):
        board = self.sudoku_board.board
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    self.assertTrue(self.sudoku_board.is_valid_move(board[i][j], i, j), f"Invalid move at ({i}, {j}) with value: {board[i][j]}")

    def test_solvable_puzzle(self):
        # This is a simplified check to ensure the puzzle can be solved
        # A more comprehensive check would involve solving the puzzle and verifying it
        board = self.sudoku_board.board
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if self.sudoku_board.is_valid_move(num, i, j):
                            break
                    else:
                        self.fail(f"No valid move found for cell ({i}, {j})")

    def test_no_duplicates_in_subgrids(self):
        board = self.sudoku_board.board
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                subgrid = [board[row][col] for row in range(start_row, start_row + 3) for col in range(start_col, start_col + 3)]
                unique_nums = [num for num in subgrid if num != 0]
                self.assertEqual(len(set(unique_nums)), len(unique_nums), f"Duplicates found in subgrid: {subgrid}")

if __name__ == '__main__':
    unittest.main()
