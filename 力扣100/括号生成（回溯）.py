from codecs import namereplace_errors
from typing import List

def generateParenthesis(n: int) -> List[str]:
    if n <= 0:
        return []

    res = []
    path = []

    def backtrack(left: int, right: int):
        if left == n and right == n:
            res.append(''.join(path.copy()))
            return

        if left < n:
            path.append('(')
            backtrack(left + 1, right)
            path.pop()

        if right < left:
            path.append(')')
            backtrack(left, right + 1)
            path.pop()

    backtrack(0, 0)
    return res