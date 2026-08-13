# 哈希表 注意：在python中，哈希表的实现就是字典和集合
# 哈希表是一种通过key直接访问value的数据结构
from typing import List

def twosum(nums: List[int], target: int) -> List[int]:
    hashtable = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashtable:      # 检查键是否存在
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []







