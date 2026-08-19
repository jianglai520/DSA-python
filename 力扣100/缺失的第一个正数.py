from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    num_set = set(nums)
    i = 1
    while i in num_set:
        i += 1
    return i

print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([2, 3, 4, 7]))