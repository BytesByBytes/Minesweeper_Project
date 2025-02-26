class Board:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = self.generate_board()
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def generate_board(self):
        import random
        
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        mines_placed = 0
        
        while mines_placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if board[y][x] != '*':
                board[y][x] = '*'
                mines_placed += 1
                self.increment_adjacent_cells(board, x, y)
        
        return board

    def increment_adjacent_cells(self, board, x, y):
        for i in range(max(0, y - 1), min(self.height, y + 2)):
            for j in range(max(0, x - 1), min(self.width, x + 2)):
                if board[i][j] != '*':
                    if board[i][j] == ' ':
                        board[i][j] = '1'
                    else:
                        board[i][j] = str(int(board[i][j]) + 1)

    def reveal_cell(self, x, y):
        if self.revealed[y][x]:
            return
        
        self.revealed[y][x] = True
        
        if self.board[y][x] == ' ':
            for i in range(max(0, y - 1), min(self.height, y + 2)):
                for j in range(max(0, x - 1), min(self.width, x + 2)):
                    self.reveal_cell(j, i)

    def is_mine(self, x, y):
        return self.board[y][x] == '*'

    def display_board(self):
        display = ''
        for i in range(self.height):
            for j in range(self.width):
                if self.revealed[i][j]:
                    display += self.board[i][j] + ' '
                else:
                    display += '# '
            display += '\n'
        return display.strip()