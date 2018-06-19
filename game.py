from contextlib import suppress

EMPTY = 'Empty'
WHITE = 'White'
BLACK = 'Black'


def has_move(board: list, line: int, column: int) -> bool:
    """
    Given a board with Black, White, and Empty Slot.Create function that calculates if starting from line and column
    defined as parameters there are empty slots that can be occupied. Imagine each player start with a position
    occupied.So the first can occupy any adjacent Empty slot.After that the second player can do the same and so on
    until there is no more Empty slot adjacent to any occopied one.
    :param board: Matrix m x n
    :param line: The line of start slot
    :param column: The column of start slot
    :return: True if there is any Empty slot adjacent to the are occupied by one
    player
    """
    return len(get_adjacents(board, line, column)) > 0


def get_adjacents(board: list, line: int, column: int):
    points = []
    board_size = len(board)
    for l in range(-1, 2):
        for c in range(-1, 2):
            line_possible = 0 <= line + l < board_size
            column_possible = 0 <= column + c < board_size
            if line_possible and column_possible and board[line + l][column + c] == EMPTY:
                points.append((line + l, column + c))

    return points
