"""
思想：分治法，先拆成两半分别排序，再合并两个有序序列
时间复杂度：O(n log n)（稳定）
特点：稳定，需要额外空间
"""

from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 测试
if __name__ == "__main__":
    test_list = [5, 3, 8, 1]
    print(merge_sort(test_list))