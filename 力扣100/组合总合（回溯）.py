from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    path = []

    def backtrack(start_index: int, remaining: int):
        if remaining == 0:
            res.append(path.copy())
            return

        if remaining < 0:
            return

        for i in range(start_index, len(candidates)):
            if candidates[i] > remaining:
                continue

            path.append(candidates[i])

            backtrack(i, remaining - candidates[i])
            path.pop()

    backtrack(0, target)
    return res