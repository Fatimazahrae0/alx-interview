#!/usr/bin/python3
import sys

def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row, n):
    if row == n:
        # Convert board to the required format
        solution = [[i, board[i].index(1)] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0

def nqueens(N):
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board
    board = [[0] * N for _ in range(N)]
    solve_nqueens(board, 0, N)
