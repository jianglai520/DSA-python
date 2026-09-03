from typing import List

def maxProduct(nums: List[int]) -> int:
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]

    for num in nums[1:]:
        prev_max = max_prod
        prev_min = min_prod

        max_prod = max(num, prev_max * num, prev_min * num)
        min_prod = min(num, prev_max * num, prev_min * num)

        result = max(max_prod, result)

    return result