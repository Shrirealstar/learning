def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col):
    # Base case: If all queens are placed, return True
    if col >= len(board):
        return True

    # Try placing a queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 'Q'
            
            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[i][col] = '.'

    return False

def solve_n_queens(n):
    # Initialize the board
    board = [['.' for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

# Solve the 8-Queens problem
solve_n_queens(8)
