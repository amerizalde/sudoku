from sudoku_board import SudokuBoard
from player_ai import PlayerAI

def test_player_ai():
    board = SudokuBoard(None)  # Create an empty board for testing
    ai_player = PlayerAI(board)

    initial_empty_cells = sum(row.count(0) for row in board.board)
    print(f"Initial empty cells: {initial_empty_cells}")

    ai_player.solve_puzzle()

    final_empty_cells = sum(row.count(0) for row in board.board)
    print(f"Final empty cells: {final_empty_cells}")

    # Show the solved board
    print("Solved Board:")
    for row in board.board:
        print(row)

    # Test whether the state of board.board represents a valid Sudoku solution
    if not is_valid_sudoku_solution(board.board):
        print("The AI's solution is invalid. Please try again.")
    else:
        print("The AI's solution is valid.")

def is_valid_sudoku_solution(board):
    # Check for duplicates in rows, columns and subgrids
    for i in range(9):
        if not is_unique(board[i]) or not is_unique([board[j][i] for j in range(9)]):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [board[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
            if not is_unique(box):
                return False

    return True

def is_unique(lst):
    # Check if all elements are unique (ignoring zeros)
    lst = [x for x in lst if x != 0]
    return len(set(lst)) == len(lst)

if __name__ == "__main__":
    test_player_ai()
