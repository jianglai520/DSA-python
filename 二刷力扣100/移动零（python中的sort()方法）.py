from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort(key = bool, reverse = True)
