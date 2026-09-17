from collections import deque
import sys

def main():
    data = sys.stdin.buffer.read().split()

    n, m, x1, y1 = int(data[0]), int(data[1]), int(data[2]), int(data[3])
    x2, y2 = int(data[4]), int(data[5])

    if x1 == x2 and y1 == y2:
        print(0)
        return

    directions = [
        (1, 2), (1, -2), (-1, 2), (-1, -2),
        (2, 1), (2, -1), (-2, 1), (-2, -1)
    ]

    visited = [[False] * m for _ in range(n)]
    visited[x1][y1] = True

    queue = deque([(x1, y1, 0)])

    while queue:
        x, y, steps = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if nx == x2 and ny == y2:
                    print(steps + 1)
                    return
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    print(0)

if __name__ == "__main__":
    main()





