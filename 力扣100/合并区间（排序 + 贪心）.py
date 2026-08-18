from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key = lambda x: x[0])

    result = []
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))

