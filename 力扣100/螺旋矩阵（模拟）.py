from typing import List

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    new_matrix = []

    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            new_matrix.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            new_matrix.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                new_matrix.append(matrix[bottom][col])
        bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                new_matrix.append(matrix[left][row])
        left += 1
    return new_matrix