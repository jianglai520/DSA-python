from typing import List

def moveZeroes(nums: List[int]) -> None:
    n = len(nums)
    j = 0
    # 记住：nums[j] 永远指向第一个0的位置，i不断往后扫描，遇到非0就和交换

    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1


"""
i = 0
j = 0
nums = [0, 1, 0, 3, 12]
nums[0] = 0 

j = 0
i = 1
nums[1] = 1 != 0
nums[0] = 1
nums[1] = 0


"""