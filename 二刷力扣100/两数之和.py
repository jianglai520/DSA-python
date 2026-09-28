# 哈希映射
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable = dict()

    for i, num in enumerate(nums):
        if (target - num) in hashtable:
            return [i, hashtable[target - num]]
        hashtable[num] = i
    return []

# 测试
if __name__ == "__main__":
    nums = [1, 3, 5]
    target = 4
    print(twoSum(nums, target))



