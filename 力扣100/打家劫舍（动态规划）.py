from typing import List

def rob(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] nums[0]

