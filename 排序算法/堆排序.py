"""
思想：利用最大堆（或者最小堆）特性，每次把堆顶（最大 or 最小）取出
时间复杂度：O(n log n)
特点：不稳定，但原地排序空间复杂度O(1)
注意点：python中没有现成的最大堆，需要加负号处理问题
"""

from typing import List
import heapq

def heap_sort(arr: List[int]) -> List[int]:
    heapq.heapify(arr)   # 建立最小堆
    return [heapq.heappop(arr) for _ in range(len(arr))]

# 测试
if __name__ == "__main__":
    arr = [6, 3, 1, -1]
    print(heap_sort(arr))