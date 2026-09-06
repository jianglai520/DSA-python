from typing import List

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()

    n = len(nums)
    left, right = 0, n - 1

    if n % 2 != 0:
        return nums[(left + right) // 2]
    else:
        return (nums[((left + right) // 2)] + nums[((left + right) // 2 + 1)]) / 2