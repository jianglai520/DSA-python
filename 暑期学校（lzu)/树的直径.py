from collections import deque
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    def bfs(start):
        dist = [-1] * (n+1)
        dist[start] = 0
        q = deque([start])
        far = start
        while q:
            u = q.popleft()
            if dist[u] > dist[far]:
                far = u
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return far, dist

    u, _ = bfs(1)
    v, dist = bfs(u)
    print(dist[v])

if __name__ == "__main__":
    main()