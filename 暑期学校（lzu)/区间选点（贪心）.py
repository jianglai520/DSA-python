"""
贪心策略：
1)将所有区间按照右端点从小到大排序
2)从第一个区间开始，选择当前区间的右端点作为一个选点
3)跳过所有包含这个点的区间（即左端点 ≤ 当前选点）
4)对于下一个不包含该点的区间，重复步骤2

对应力扣：452用最少数量的箭引爆气球
"""

import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    intervals = []

    for _ in range(n):
        a,b = map(int, input().split())
        intervals.append((a, b))

    intervals.sort(key = lambda x: x[1])

    count = 0
    last_point = float('-inf')

    for a, b in intervals:
        if a > last_point:
            count += 1
            last_point = b

    print(count)

if __name__ == "__main__":
    main()

