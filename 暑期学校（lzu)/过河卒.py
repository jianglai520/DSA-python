def main():
    n, m, x, y = map(int, input().split())

    horse = set()
    horse.add((x, y))
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        horse.add((nx, ny))

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    if (0, 0) not in horse:
        dp[0][0] = 1

    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) in horse:
                dp[i][j] = 0
                continue
            if i == 0 and j == 0:
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    print(dp[n][m])

if __name__ == "__main__":
    main()