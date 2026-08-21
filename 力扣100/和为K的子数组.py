from typing import List
from collections import defaultdict

def subarraySum(nums: List[int], k: int) -> int:
    prefix_sum_count = defaultdict(int)

    prefix_sum_count[0] = 1
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        need = current_sum - k
        count += prefix_sum_count.get(need, 0)

        prefix_sum_count[current_sum] += 1

    return count

# 测试
nums = [1,1,1]
k = 2
print(subarraySum(nums, k))