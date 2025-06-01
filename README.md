# Sudoku Game (Tkinter)

A desktop Sudoku game built with Python and Tkinter. This application generates a new Sudoku puzzle each time, provides a user-friendly interface for solving it, and includes a menu with the rules of Sudoku. The project also features unit tests and continuous integration via GitHub Actions.

## Features
- Randomly generated Sudoku puzzles
- Interactive 9x9 board with input validation
- Check your solution for correctness
- Clear the board to start over
- Help menu with Sudoku rules
- Unit tests for board logic
- GitHub Actions CI for automated testing

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/sudoku.git
   cd sudoku
   ```
2. **Install Python 3.8+** (if not already installed)
3. **Install dependencies:**
   The only required dependency is Tkinter, which is included with most Python installations.

## Usage
Run the application with:
```sh
python app.py
```
A window will open with a Sudoku board. Fill in the empty cells, use the "Check" button to validate your solution, and "Clear" to reset the board. Access the rules from the Help menu.

## Testing
To run the unit tests:
```sh
python run_tests.py
```
This will execute the tests in `test_sudoku_board.py`.

## Continuous Integration
This project uses GitHub Actions to automatically run tests on push and pull requests to the `main` branch for Python 3.8 and 3.9.

## File Structure
- `app.py` — Main application entry point
- `sudoku_board.py` — Sudoku board logic and GUI
- `menu.py` — Help menu with rules
- `run_tests.py` — Test runner
- `test_sudoku_board.py` — Unit tests for board logic

## License
MIT License

## Credits
Developed by Andrew Merizalde, with aider on devstral.

---
Enjoy solving Sudoku!
