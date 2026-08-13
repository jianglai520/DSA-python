"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)

    longest_length = 1
    current_length = 1

    if n == 0:
        return 0
    else:
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current_length += 1
                longest_length = max(current_length, longest_length)
            else:
                current_length = 1
        return longest_length

print(longestConsecutive([3, 6, 1, 2]))
print(longestConsecutive([1]))
print(longestConsecutive([]))


