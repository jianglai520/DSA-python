def partitionLabels(s: str) -> List[int]:
    last = {}
    n = len(s)
    for i, ch in enumerate(s):
        last[ch] = i

    result = []
    start = 0
    end = 0

    for i in range(n):
        end = max(end, last[s[i]])

        if i == end:
            result.append(end - start + 1)
            start = end + 1
    return result