"""
思想：选一个基准（pivot)，把小于它的放左边，大于它的放右边，递归处理左右
时间复杂度：平均 O(n log n)，最坏 O(n²)（但实际很快）
特点：不稳定，但速度极快，应用最广
方法：分治法(Divide and Conquer)
核心三步：选基准；分区；递归合并
"""

from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 测试
if __name__ == "__main__":
    test_list = [5, 3, 8, 1]
    print(quick_sort(test_list))