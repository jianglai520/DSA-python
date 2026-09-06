"""
思想：每轮从未排序部分选出最小的，放到已排序末尾
时间复杂度：O(n²)
空间复杂度：O(1)，原地排序，不需要额外的数组或数据结构来存储数据
特点：不稳定，但简单，交换次数少
适合场景：
1）数据量很小
2）交换操作代价很高
3）不在乎稳定性的场景
"""

from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 测试
if __name__ == "__main__":
    test_list = [5, 3, 8, 1]
    print(selection_sort(test_list))









































