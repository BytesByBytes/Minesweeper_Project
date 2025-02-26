import random
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))) 

from game import Game

def main():
    print("Welcome to Minesweeper!")
    
    try:
        width = int(input("Enter the width of the board: "))
        height = int(input("Enter the height of the board: "))
        num_mines = int(input("Enter the number of mines: "))

        if width <= 0 or height <= 0 or num_mines <= 0 or num_mines >= width * height:
            print("Invalid board size or number of mines.")
            return
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    game = Game(width, height, num_mines)
    game.start()

    while not game.is_game_over():
        game.display_board()
        user_input = input("Enter your move (row col) or type 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting the game.")
            sys.exit()
        
        try:
            row, col = map(int, user_input.split())

            if not (0 <= row < height and 0 <= col < width):
                print("Invalid move. Enter a row and column within the board size.")
                continue

            game.reveal_cell(row, col)
        except ValueError:
            print("Invalid input. Please enter row and column as two numbers separated by a space.")

    game.display_board()  # Show final board state

    if game.has_won():
        print("Congratulations! You've cleared the minefield!")
    else:
        print("Game Over! You hit a mine.")

if __name__ == "__main__":
    main()


