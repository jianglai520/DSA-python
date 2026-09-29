"""
n * n的暴力解法，两个指针同时跑，一个不动，一个动，跑完一轮，再继续动；计算高和宽，记录最大的
时间复杂度：O(n*n)
"""
from typing import List

def maxArea(height: List[int]) -> int:
    last_max = 0

    for i in range(len(height)):
        for j in range(i+1, len(height)):
            cur_max = min(height[i], height[j]) * (j - i)
            last_max = max(cur_max, last_max)

    return last_max


# 测试
if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))