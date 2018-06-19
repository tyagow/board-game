# Board Game

    Given a board wuith Black, White, and Empty Slot. Create function that calculates
    if starting from line and column defined as parameters there are empty slots that
    can be occupied.
    
    Imagine each player start with a position occupied. So the first can occupy any 
    adjacent Empty slot. After that the second player can do the same and so on until 
    there is no more Empty slot adjacent to any occopied one.

    def has_move(board, line column):
        """
        :param board: Matrix m x n
        :param line: The line of start slot
        :param column: The column of start slot
        :return: True if there is any Empty slot adjacent to the are occupied by one
        player
        """
    