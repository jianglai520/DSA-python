# 迪杰斯特拉算法要求边权非负，这个一定要注意

import sys
import heapq

def main():
    input = sys.stdin.readline
    n, m, s, t = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[s] = 0

    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        if u == t:
            break
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    print(dist[t])

if __name__ == "__main__":
    main()