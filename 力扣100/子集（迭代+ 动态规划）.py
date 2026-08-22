from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = [[]]
    for num in nums:
        res += [cur + [num] for cur in res]

    return res

# 测试
nums = [1, 2, 3]
print(subsets(nums))