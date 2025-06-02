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
    
    # show the solved board AI!

if __name__ == "__main__":
    test_player_ai()
