"""
时间复杂度：O(n*n)
空间复杂度：O(1)
"""
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res: List[List[int]] = []

    for i in range(n - 2):    # 自动处理 n < 3的情况，减少两次无用功
        if nums[i] > 0:  # 剪枝：最小值已经 >0，那后面不可能凑出0，及时止损
            break

        if i > 0 and nums[i] == nums[i - 1]:   # 走过的路不再重复走
            continue

        left, right = i + 1, n - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])  # 找到一组之后两个指针同时移动，并跳过重复值
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res

# 测试
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
