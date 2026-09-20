import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    L = int(data[0])
    N = int(data[1])
    if N == 0:
        print("0 0")
        return
    positions = list(map(int, data[2: 2+N]))

    min_time = 0
    max_time = 0

    for p in positions:
        dist_left = p
        dist_right = L + 1 - p
        min_time = max(min_time, min(dist_left, dist_right))
        max_time = max(max_time, max(dist_left, dist_right))
    print(min_time, max_time)

if __name__ == "__main__":
    main()