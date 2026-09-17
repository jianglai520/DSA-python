import sys
from heapq import heappush, heapreplace

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    jobs = []
    idx = 1
    for _ in range(n):
        d = int(data[idx])
        p = int(data[idx + 1])
        idx += 2
        jobs.append((d, p))

    jobs.sort()

    heap = []
    total = 0
    push = heappush
    replace = heapreplace

    for d, p in jobs:
        if len(heap) < d:
            push(heap, p)
            total += p
        elif heap and heap[0] < p:
            total += p - heap[0]
            replace(heap, p)

    sys.stdout.write(str(total))

if __name__ == "__main__":
    main()