import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [[] for _ in range(n+1)]
    indeg = [0] * (n + 1)

    for _ in range(m):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        adj[x].append(y)
        indeg[y] += 1

    dp = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if indeg[i] == 0:
            q.append(i)

    ans = 0
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dp[u] + 1 > dp[v]:
                dp[v] = dp[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        if dp[u] > ans:
            ans = dp[u]

    print(ans)

if __name__ == "__main__":
    main()