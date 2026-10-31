#!/usr/bin/python3
"""Solve the N Queens problem using backtracking."""

import sys


def is_safe(board, row, col):
    """Check whether a queen can be placed safely."""
    for queen_row, queen_col in board:
        if queen_col == col:
            return False

        if abs(queen_row - row) == abs(queen_col - col):
            return False

    return True


def solve_nqueens(n, row, board):
    """Find and print all valid solutions."""
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])

            solve_nqueens(n, row + 1, board)

            board.pop()


def main():
    """Validate arguments and solve the puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n, 0, [])


if __name__ == "__main__":
    main()
