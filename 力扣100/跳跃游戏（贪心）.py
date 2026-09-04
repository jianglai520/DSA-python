from typing import List

def canJump(nums: List[int]) -> bool:
    n = len(nums)
    max_index = 0
    i = 0

    while i < n:
        if i > max_index:
            return False

        max_index = max(max_index, i + nums[i])

        if max_index >= n-1:
            return True
        i += 1