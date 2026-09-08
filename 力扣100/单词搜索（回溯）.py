from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    if not board or not board[0]:
        return False

    m, n = len(board), len(board[0])
    visited = [[False] * n for _ in range(m)]

    def backtrack(i: int, j: int, index: int) -> bool:
        if index == len(word):
            return True

        if (i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[index]):
            return False

        visited[i][j] = True

        directions = [(0, 1), (0, -1), (1, 0), (-1,0)]
        for di, dj in directions:
            if backtrack(i+di, j+dj, index+1):
                return True

        visited[i][j] = False
        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if backtrack(i, j, 0):
                    return True

    return False