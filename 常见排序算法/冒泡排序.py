"""
思想：相邻元素两两比较，大的往后“冒泡”。每轮把最大的放到底部。
时间复杂度：O(n²)
特点：简单，但效率低。
"""
from typing import List

def bubble_sort(arr: List[int]):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# 测试
if __name__ == "__main__":
    test_list = [5, 3, 8, 1]
    print(bubble_sort(test_list))

