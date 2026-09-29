"""
双指针：
用2个对向指针，最开始记录宽最大的，再通过调整高，记录最大的。
有点控制变量的感觉，一开始固定宽度（最大），比较两个指针的大小，记录一次最值，然后缩短宽，动更矮的指针，维持高指针做边，保持容量尽可能大。
"""

from typing import List

def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    last_max = 0

    while left < right:
        cur_height = min(height[left], height[right])
        cur_max = cur_height * (right - left)
        last_max = max(cur_max, last_max)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return last_max

# 测试
if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(height))
