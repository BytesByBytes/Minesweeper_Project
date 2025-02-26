import random
import sys
from game import Game

def main():
    print("Welcome to Minesweeper!")
    width = int(input("Enter the width of the board: "))
    height = int(input("Enter the height of the board: "))
    num_mines = int(input("Enter the number of mines: "))

    game = Game(width, height, num_mines)
    game.start()

    while not game.is_game_over():
        game.display_board()
        user_input = input("Enter your move (row col): ")
        if user_input.lower() == 'exit':
            print("Exiting the game.")
            sys.exit()
        
        try:
            row, col = map(int, user_input.split())
            game.reveal_cell(row, col)
        except ValueError:
            print("Invalid input. Please enter row and column as two numbers separated by a space.")

    if game.has_won():
        print("Congratulations! You've cleared the minefield!")
    else:
        print("Game Over! You hit a mine.")

if __name__ == "__main__":
    main()