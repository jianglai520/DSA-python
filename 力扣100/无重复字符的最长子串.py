from typing import List

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0
    n = len(s)

    for right in range(n):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right

        current_lenght = right - left + 1
        max_length = max(max_length, current_lenght)

    return max_length

print(lengthOfLongestSubstring("abcabcbb"))