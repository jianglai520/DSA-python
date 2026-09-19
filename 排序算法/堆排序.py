"""
思想：利用最大堆（或者最小堆）特性，每次把堆顶（最大 or 最小）取出
时间复杂度：O(n log n)
特点：不稳定，但原地排序空间复杂度O(1)
"""

from typing import List
import heapq

def heap_sort(arr: List[int]) -> List[int]:
    heapq.heapify(arr)   # 建立最小堆
    return [heapq.heappop(arr) for _ in range(len(arr))]