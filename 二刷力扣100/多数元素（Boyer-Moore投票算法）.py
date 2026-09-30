"""
时间复杂度：O(n)
空间复杂度：O(1)

核心思想：
维护一个候选元素 candidate 和计数器 conut
遇到相同元素 count += 1
遇到不同元素 count -= 1
当 count == 0时，更换候选元素
最终留下的候选元素就是多数元素
"""

from typing import List

def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = nums[0]

    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
