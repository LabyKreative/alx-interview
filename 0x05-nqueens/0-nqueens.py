#!/usr/bin/python3
"""A program that solves the N queens problem."""
import sys


def place_queens(r, n, cols, pos, neg, board):
    """
    Backtrack function to find solutions to the N-Queens problem.

    Args:
        r (int): Current row.
        n (int): Total number of rows/columns on the chessboard.
        cols (set): Set of used columns.
        pos (set): Set of used positive diagonals.
        neg (set): Set of used negative diagonals.
        board (list): Current state of the chessboard.

    Returns:
        None (prints solutions).
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        place_queens(r + 1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def solve_nqueens(n):
    """
    Solves the N-Queens problem and prints all possible solutions.

    Args:
        n (int): Number of queens. Must be >= 4.

    Returns:
        None (prints solutions).
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    place_queens(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        solve_nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
