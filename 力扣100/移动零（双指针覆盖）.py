from typing import List

def moveZeros(nums: List[int]) -> None:
    slow = 0
    n = len(nums)
    for fast in range(n):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1

    for i in range(slow, n):
        nums[i] = 0




"""
slow = 0
fast = 0 
nums[0] != 0
nums[0] = nums[0]
slow = 1

slow = 1
...
"""