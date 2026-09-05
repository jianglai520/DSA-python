from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left = findLeft(nums, target)
    right = findRight(nums, target)

    if left <= right and nums[left] == target:
        return [left, right]
    else:
        return [-1,-1]
