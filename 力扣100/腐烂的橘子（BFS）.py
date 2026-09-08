from typing import List
from collections import deque

def orangeRotting(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return -1

    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh_count += 1
            elif grid[i][j] == 2:
                queue.append((i, j))

    if fresh_count == 0:
        return 0

    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue and fresh_count > 0:
        minutes += 1

        level_size = len(queue)

        for _ in range(level_size):
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    queue.append((nx, ny))

    return minutes if fresh_count == 0 else -1