from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort()

    return nums[-k]