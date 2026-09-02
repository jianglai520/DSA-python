def numSquares(n: int) -> int:
    dp = [0] * (n + 1)

    for i in range(1, n+1):
        dp[i] = i

        j = 1
        while j * j <= i:
            dp[i] = min(dp[i-j*j] + 1, dp[i])
            j += 1
    return dp[n]