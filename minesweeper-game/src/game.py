class Game:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.mines = set()  # Store mines as a set of (row, col) tuples
        self.game_over = False
        self.initialize_board()
        
    def start(self):
        # Start the game (you can add custom logic here if needed)
        print("The game has started!")
        self.display_board()  # Display the board when the game starts

    def initialize_board(self):
        import random
        while len(self.mines) < self.num_mines:
            r, c = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            self.mines.add((r, c))

    def reveal_cell(self, row, col):
        if (row, col) in self.mines:
            self.game_over = True
            print("Boom! You hit a mine.")
        else:
            self.board[row][col] = '0'  # Placeholder for now
            print(f"Revealed ({row}, {col})")

    def is_game_over(self):
        return self.game_over

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def has_won(self):
        return False  # Update this logic properly
