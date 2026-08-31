# 暴力解法违反规定（题目要求使用原地算法）
from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead
    """
    m, n = len(matrix), len(matrix[0])

    zero_positions = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))

    for row, col in zero_positions:
        for j in range(n):
            matrix[row][j] = 0
        for i in range(m):
            matrix[i][row] = 0