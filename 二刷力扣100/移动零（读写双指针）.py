"""
时间复杂度：O(n)
空间复杂度：O(1)
"""
from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    j = 0               # 写指针：下一个“合格元素”的位置

    for i in range(n):   # 读指针：扫描
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
