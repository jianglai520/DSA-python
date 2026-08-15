from typing import List


def threeSum(nums: list[int]) -> list[list[int]]:
    new_nums = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (i != j) and (i != k) and (j != k):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sub = sorted([nums[i], nums[j], nums[k]])
                        if sub not in new_nums:
                            new_nums.append(sub)
    return new_nums

print(threeSum([-1, 0, 1, 2, -1, -4]))