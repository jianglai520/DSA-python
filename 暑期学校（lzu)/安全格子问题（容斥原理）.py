"""
基本思路就是：总的方格数 - 被行覆盖的 - 被列覆盖的 + 被重复减去的交叉点
相似力扣题目：LCP 22.黑白方格画
"""

import sys

def main():
    input = sys.stdin.readline
    n, m, q = map(int, input().split())

    rows = set()   # 注意：别踩坑，这里就是要用set,防止相同的行或则列重复计算
    cols = set()

    for _ in range(q):
        t, c = map(int, input().split())
        if t == 0:
            rows.add(c)
        else:
            cols.add(c)

    r, c = len(rows), len(cols)

    safe = n * m - r * n - c * m + r * c
    print(safe)

if __name__ == "__main__":
    main()

