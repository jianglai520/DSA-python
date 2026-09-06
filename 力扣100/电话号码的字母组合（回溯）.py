from typing import List

def letterCombinations(digits: str) -> List[int]:
    if not digits:
        return []

    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    res = []
    path = []

    def backtrack(index):
        if index == len(digits):
            res.append(''.join(digits))
            return

        letters = phone[digits[index]]

        for letter in letters:
            path.append(letter)

            backtrack(index + 1)

            path.pop()
    backtrack(0)
    return res