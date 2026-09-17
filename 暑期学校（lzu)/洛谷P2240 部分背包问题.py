"""
本题目关键词：所有金币都可以随意分割，分割完的金币重量价值比不变

意味着每堆金币可以拿一部分，按比例算钱（部分背包问题）
我们用贪心解决(因为金币可以分割，我们优先要拿单位重量价值最高的金币（首页算每堆金币的“性价比”）；然后按照性价比从高到低排序；能拿整堆就拿整堆；如果背包剩余容量不够拿一整堆，就拿一部分，直到背包装满
"""

import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    items = []
    for _ in range(n):
        m = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        items.append((v / m, m , v))

    items.sort(key = lambda x: x[0], reverse = True)

    total = 0.0
    for ratio, m, v in items:
        if t >= m:
            total += v
            t -= m
        else:
            total += ratio * t
            break
    print(f"{total:.2f}")

main()

