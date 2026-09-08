from typing import List

def partition(s: str) -> List[List[str]]:
    if not s:
        return [[]]

    res = []
    path = []

    def is_palindrome(sub: str):
        return sub == sub[::-1]

    def backtrack(start: int):
        if start == len(s):
            res.append(path[:])

        for end in range(start, len(s)):
            sub = s[start: end+1]

            if is_palindrome(sub):
                path.append(sub)
                backtrack(end+1)
                path.pop()

    backtrack(0)
    return res
