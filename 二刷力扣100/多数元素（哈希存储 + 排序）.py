"""
题干：给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。你可以假设数组是非空的，并且给定的数组总是存在多数元素。
本题很基础的题目，一定要会
"""

from typing import List

def majorityElement(nums: List[int]) -> int:
    if not nums:
        return 0

    dit = {}
    for num in nums:
        dit[num] = dit.get(num, 0) + 1

    sorted_dit = sorted(dit.items(), key = lambda x: x[1], reverse = True)
    return sorted_dit[0][0]


# 测试
if __name__ == "__main__":
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))