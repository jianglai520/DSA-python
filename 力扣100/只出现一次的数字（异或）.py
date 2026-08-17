from typing import List

def singleNumber(nums: List[int]) -> int:
    result = 0
    for i in nums:
        result ^= i
    return result


print(singleNumber([1, 2, 2]))
print(singleNumber([3, 3, 4, 4, 2]))