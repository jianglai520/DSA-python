import sys
import heapq

def main():
    input = sys.stdin.readline
    n, m, s = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0

    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (dist[v], v))

    ans = []
    for i in range(1, n + 1):
        if dist[i] == INF:
            ans.append("2147483647")
        else:
            ans.append(str(dist[i]))

    sys.stdout.write(" ".join(ans))

if __name__ == "__main__":
    main()

