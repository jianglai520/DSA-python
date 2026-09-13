import sys

# 超时
def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    max_list = []
    min_list = []

    for i in range(n-k+1):
        window = a[i:i+k]
        max_list.append(max(window))
        min_list.append(min(window))

    print(" ".join(map(str, max_list)))
    print(" ".join(map(str, min_list)))

if __name__ == "__main__":
    main()