from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    sorted_items = sorted(count.items(), key = lambda x: x[1], reverse = True)

    return [num for num, freq in sorted_items[:k]]