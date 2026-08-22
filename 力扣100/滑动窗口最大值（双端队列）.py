from typing import List
from collections import deque

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    if not nums or k == 0:
        return []

    dq = deque()
    result = []

    for i, num in enumerate(nums):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

# 测试
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))