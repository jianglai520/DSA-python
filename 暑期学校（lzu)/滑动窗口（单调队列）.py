import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    min_list = []
    max_list = []

    dq = deque()
    for i in range(n):
        while dq and a[dq[-1]] >= a[i]:
            dq.pop()
        dq.append(i)

        if dq[0] <= i-k:
            dq.popleft()

        if i >= k-1:
            min_list.append(a[dq[0]])

    dq = deque()
    for i in range(n):
        while dq and a[dq[-1]] <= a[i]:
            dq.pop()
        dq.append(i)

        if dq[0] <= i-k:
            dq.popleft()

        if i >= k-1:
            max_list.append(a[dq[0]])

    print(" ".join(map(str, min_list)))
    print(" ".join(map(str, max_list)))

if __name__ == "__main__":
    main()