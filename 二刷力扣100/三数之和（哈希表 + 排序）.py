"""
时间复杂度：O(n*n)
空间复杂度：O(n*n)

"""
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res, seen = set(), set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            target = -(nums[i] + nums[j])
            if target in seen:
                res.add((target, nums[i], nums[j]))
        seen.add(nums[i])
    return [list(i) for i in res]

# 测试
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))

