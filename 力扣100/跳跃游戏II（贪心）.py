from typing import List

def jump(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return 0

    jump = 0
    current_end = 0
    farthest = 0

    for i in range(n-1):
        farthest = max(farthest, i + nums[i])

        if i == current_end:
            jump += 1
            current_end = farthest

            if current_end >= n-1:
                break
    return jump