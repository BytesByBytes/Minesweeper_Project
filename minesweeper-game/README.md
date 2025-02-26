# Minesweeper Game Project File Structure

## board.py
- Class `Board`:
  - `__init__(self, width, height, num_mines)`: Initializes the board with given dimensions and number of mines.
  - `generate_board(self)`: Generates the board with mines and numbers.
  - `increment_adjacent_cells(self, board, x, y)`: Increments the numbers in adjacent cells around a mine.
  - `reveal_cell(self, x, y)`: Reveals a cell and recursively reveals adjacent cells if the cell is empty.
  - `is_mine(self, x, y)`: Checks if a cell contains a mine.
  - `display_board(self)`: Returns a string representation of the board for display.

## game.py
- Class `Game`:
  - `__init__(self, width, height, num_mines)`: Initializes the game with a board.
  - `play(self)`: Main game loop to handle user input and game logic.
  - `check_win(self)`: Checks if the player has won the game.
  - `end_game(self, won)`: Ends the game and displays the final board.

## main.py
- Main entry point of the game:
  - `if __name__ == "__main__":`: Initializes and starts the game.

## utils.py
- Utility functions:
  - `parse_input(input_str)`: Parses user input for coordinates.
  - `validate_input(x, y, width, height)`: Validates user input coordinates.

## constants.py
- Game constants:
  - `WIDTH`: Default width of the board.
  - `HEIGHT`: Default height of the board.
  - `NUM_MINES`: Default number of mines.