from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])

    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        val = matrix[mid // 2][mid % 2]

        if val > target:
            right = mid - 1
        elif val < target:
            left = mid + 1
        else:
            return True
    return False