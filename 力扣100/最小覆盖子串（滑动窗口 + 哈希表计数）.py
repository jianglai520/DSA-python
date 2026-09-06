def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    left = 0
    right = 0
    formed = 0
    required = len(need)

    min_len = float('inf')
    min_start = 0

    while right < len(s):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] == need[ch]:
            formed += 1

        while formed == required and left <= right:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left

            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -= 1
            left += 1

        right += 1
    return "" if min_len == float('inf') else s[min_start: min_start + min_len]
