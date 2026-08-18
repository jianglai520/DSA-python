from typing import List

def majortyElement(nums: List[int]) -> int:
    candidate =  nums[0]
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


print(majortyElement([3, 2, 3]))
print(majortyElement([2, 2, 1, 1, 1, 2, 2]))