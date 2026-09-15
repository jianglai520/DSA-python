# 本题目内存限制64KB，python版本代码无论如何优化都通不过
"""
python是“开发效率优先”的语言，C/C++是“运行效率优先”的语言
根据场景要切换适合的语言
"""

import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    heights = list(map(int, input().split()))

    lo, hi = 0, max(heights)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        total = 0
        for h in heights:
            if h > mid:
                total += h - mid

        if total >= M:
            lo = mid
        else:
            hi = mid - 1
    print(lo)

if __name__ == "__main__":
    main()