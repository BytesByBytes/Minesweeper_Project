def validate_input(user_input, board_size):
    try:
        x, y = map(int, user_input.split(','))
        if 0 <= x < board_size and 0 <= y < board_size:
            return (x, y)
        else:
            return None
    except ValueError:
        return None

def display_board(board):
    for row in board:
        print(' '.join(row))