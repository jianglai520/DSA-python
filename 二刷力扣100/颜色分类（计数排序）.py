"""
计数排序：统计每个颜色出现了多少次，然后按照次数重写数组
两次遍历时间复杂度 O(n) 空间O(1)  -- 不是很推荐
"""

from typing import List

def sortColor(nums: List[int]) -> None:
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1

    idx = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[idx] = color
            idx += 1