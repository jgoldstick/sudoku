#!/usr/bin/env python3
import time

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
        self.all_candidates = set('123456789')
        # print(self.board)
        for r in range(1, 10):
            for c in range(1, 10):
                # print(r, c, start_values.keys())
                if (r, c) in start_values.keys():
                    self.board[r-1][c-1] = start_values[(r, c)]

    def taken_values_row(self, row):
        """
        given a row, return a set of all the values taken in the row
        """

        used_set = set()
        used_set = set(self.board[row-1]) - set(' ')
        return used_set

    def taken_col(self, col):
        used_set = set()
        for r in range(9):
            used_set.add(self.board[r][col-1])
        return used_set - set(' ')

    def taken_values_box(self, row, col):
        row, col = self.box(row, col)
        used_set = set()
        for r in range(row, row+3):
            for c in range(col, col+3):
                used_set.add(self.board[r][c])
        return used_set - set(' ')

    def taken_values(self, row, col):
        used_set = self.taken_values_row(row)
        used_set |= self.taken_col(col)
        used_set |= self.taken_values_box(row, col)
        # print("row: {}, col: {} used values are ".format(row, col, used_set))
        return used_set - set(' ')

    def box(self, r, c):
        """
        box takes a row and column (1-9 based)
        and returns the row and column (0-8 based) which is the lower bound for
        the 3 by 3 box that row/col is contained within
        """

        lower_col = (c-1)//3*3
        lower_row = (r-1)//3*3
        return lower_row, lower_col


def populate_board():
    start_values = {}
    for i in range(10):
        prompt = "Enter spaces or initial values  followed by a comma for row "
        line = input(prompt + str(i+1))
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


def print_board(board):
    for row in board:
        print(row)


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
    print_board(sudoku.board)

    working = True
    while working:
        working = False
        for r in range(1, 10):
            for c in range(1, 10):
                # print(sudoku.taken_values(r, c))
                possible = sudoku.all_candidates - sudoku.taken_values(r, c)
                # print(possible)
                if len(possible) == 1:
                    working = True
                    print(r, c)
                    sudoku.board[r-1][c-1] = possible.pop()
                    print("------------------------we have a new box", possible)
                    print("new board:")
                    print_board(sudoku.board)
                    time.sleep(1)


if __name__ == "__main__":
    main()
