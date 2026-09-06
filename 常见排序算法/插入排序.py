"""
思想：像打扑克牌，每张新牌插入到前面已经排序的合适位置
时间复杂度：O(n²)
空间复杂度：O(1)
特点：稳定，适合小数据
核心：
1）假设前面已经排好序
2）取一下元素，找到正确位置插入
3）移动元素腾出空间
4）重复直到全部排好
"""

from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# 测试
if __name__ == "__main__":
    test_list = [5, 3, 8, 1]
    print(insertion_sort(test_list))








































