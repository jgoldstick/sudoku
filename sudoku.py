#!/usr/bin/env python3

"""
Sudoku --  a program to solve sudoku puzzles

Sudoku is a 9 x 9 matrix of blanks and pre-initialized numbers.
The matrix is further divided into 9 3 x 3 matrices.  When solved,
each of the 9 rows will contain the numbers 1 through 9 with no repeats.
Likewise, for the columns.  Each of the 9 contained matrices will also
contain the numbers 1 through 9.
"""


class Sudoku(object):
    def __init__(self, start_values):
        """
        start_values are a dictionary with keys being a tuple representing
        the position in the rows and columns where the value should be
        stored
        """

        self.board = [["" for i in range(9)] for j in range(9)]
        print("Initial Board")
        # print(self.board)
        for r in range(1, 10):
            for c in range(1, 10):
                # print(r, c, start_values.keys())
                if (r, c) in start_values.keys():
                    self.board[r-1][c-1] = start_values[(r, c)]

    def taken_values(self, row, col):
        used_set = set()
        used_set = set(self.board[row-1])
        print(used_set)
        for r in range(9):
            used_set.add(self.board[r][col-1])
        print(used_set)
        return used_set - set(' ')


def populate_board():
    start_values = {}
    for i in range(10):
        line = input("Enter spaces or initial values  followed by a comma for row " + str(i))
        row = line.split(',')
        for r, c in enumerate(row):
            start_values[(i+1, r+1)] = c
        print(row)
    return start_values


def box(r, c):
    """
    box takes a row and column (1-9 based)
    and returns the row and column (0-8 based) which is the lower bound for
    the 3 by 3 box that row/col is contained within
    """

    lower_col = (c-1)//3*3
    lower_row = (r-1)//3*3
    return lower_row, lower_col


def main():
    start_values = populate_board()
    """
    start_values = {}
    start_values[(1, 1)] = 1
    start_values[(2, 2)] = 2
    """
    for row in start_values:
        print(row)
    sudoku = Sudoku(start_values)
    for row in sudoku.board:
        print(row)

    print(sudoku.taken_values(1, 1))

if __name__ == "__main__":
    main()
