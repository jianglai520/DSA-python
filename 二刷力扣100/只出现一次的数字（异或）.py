"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

这道题目主要考察位运算（异或）
任何数和自己异或为0
任何数字和0异或为它本身
"""

from typing import List

def singleNumber(nums: List[int]) -> int:
    res = 0
    for i in nums:
        res ^= i
    return res

# 测试
if __name__ == "__main__":
    nums = [2, 2, 1]
    print(singleNumber(nums))