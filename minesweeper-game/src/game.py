class Game:
    def __init__(self, board):
        self.board = board
        self.game_over = False
        self.won = False

    def start_game(self):
        self.board.generate_board()
        print("Game started! Good luck!")

    def reveal_cell(self, x, y):
        if self.board.is_mine(x, y):
            self.game_over = True
            print("Game Over! You hit a mine.")
        else:
            self.board.reveal_cell(x, y)
            if self.board.check_win_condition():
                self.won = True
                print("Congratulations! You've won the game.")

    def check_game_status(self):
        if self.game_over:
            return "Game Over"
        elif self.won:
            return "You Won"
        return "In Progress"