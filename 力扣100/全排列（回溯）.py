from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res = []
    path = []

    def backtrack():
        if len(path) == len(nums):
            res.append(path.copy())
            return

        for i in range(len(nums)):
            if nums[i] in path:
                continue

            path.append(nums[i])
            backtrack()
            path.pop()

    backtrack()
    return res