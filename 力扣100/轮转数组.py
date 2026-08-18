from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

nums1 = [1,2,3,4,5,6,7]
rotate(nums1, 3)
print(nums1)  # [5,6,7,1,2,3,4]

nums2 = [-1,-100,3,99]
rotate(nums2, 2)
print(nums2)  # [3,99,-1,-100]

nums3 = [1,2,3,4,5]
rotate(nums3, 7)
print(nums3)  # [4,5,1,2,3] 因为 7%5=2