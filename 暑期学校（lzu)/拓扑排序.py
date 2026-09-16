import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    queue = deque(i for i in range(1, N+1) if indegree[i] == 0)

    result = []
    while queue:
        u = queue.popleft()
        result.append(u)

        for nxt in graph[u]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()