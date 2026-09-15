import heapq
import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))

    heapq.heapify(nums)   # 把列表调整成小顶堆，当然在python中只有小顶堆

    ans = 0
    while len(nums) > 1:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        s = x + y
        ans += s
        heapq.heappush(nums, s)

    print(ans)

if __name__ == "__main__":
    main()
