from typing import List

def solveNQueens(n: int) -> List[List[int]]:
    if n <= 0:
        return []

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    diag1 = set()
    diag2 = set()

    def is_not_under_attack(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def place_queen(row, col):
        cols.add(col)
        diag1.add(row-col)
        diag2.add(row+col)
        board[row][col] = 'Q'

    def remove_queen(row, col):
        cols.remove(col)
        diag1.remove(row-col)
        diag2.remove(row+col)
        board[row][col] = '.'

    def backtrack(row):
        if row == n:
            result.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                backtrack(row+1)
                remove_queen(row, col)

    backtrack(0)
    return result