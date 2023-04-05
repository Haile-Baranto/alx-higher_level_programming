#!/usr/bin/python3
import sys
""" The module solves solves the N queens problem.

Usage: nqueens N
You are only allowed to import the sys module
    """


def nqueens(n):
    """queens(n) akes an integer n as input and
    returns a list of solutions to the N Queens problem.

    Args:
        n (int): The number of quens in n * n chess
    """
    def is_valid(board, row, col):
        for r, c in board:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(board, row):
        nonlocal n, solutions
        if row == n:
            solutions.append(board[:])
        else:
            for col in range(n):
                if is_valid(board, row, col):
                    board.append((row, col))
                    backtrack(board, row+1)
                    board.pop()

    solutions = []
    backtrack([], 0)

    for sol in solutions:
        print(sol)


if __name__ == "__main__":
    """ checks if user input consists only two arguements including program
    name. if not print "Usage: nqueens N" and exit with status code 1
        """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    """ checks if user input is an integer if not print massage and
    exit the program with status code 1
        """
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """ check if user input is < 4. if so print N must be at least 4
    and exit the program with status code 1
        """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)
