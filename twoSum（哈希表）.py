# 哈希表
from typing import List

def twosum(nums: List[int], target: int) -> List[int]:
    hashtable = {}

    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []

print(twosum([2, 7, 11, 15], 9))