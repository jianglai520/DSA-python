"""
时间复杂度：O(n)
空间复杂度：O(1)
这道接雨水用双指针最优，面试首选
思路：
不要去想水怎么流，而是去想“每个位置能存多少水”；
对于第i个位置（宽度为1），它能存的水量是： water[i] = min(左边最高柱子，右边最高柱子) - height[i]
那这道题目的难点就成了：如何高效求出每个位置的“左边最大值”和“右边最大值”

设 left_max 为左指针扫过的最大值，right_max 为右指针扫过的最大值。当 height[left] < height[right] 时：
左指针位置的水量只由 left_max 决定，因为右边一定存在一个不低于 height[left]（实际是 ≥ height[right] > height[left]）的柱子当挡板，右侧不会成为瓶颈。
反之，右指针位置的水量只由 right_max 决定。
"""

from typing import List

def trap(height: List[int]) -> int:
    n = len(height)
    if not height:
        return 0

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# 测试
if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))

