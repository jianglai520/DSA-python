"""
思想：相邻元素两两比较，大的往后“冒泡”。每轮把最大的放到底部。
时间复杂度：O(n²)
特点：简单，但效率低。
算法步骤：
1）比较相邻的元素。如果第一个比第二个大（升序），就交换它们的位置
2）对每一个相邻元素做同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数
3）针对所有的元素重复以上的步骤，除了最后一个（因为每一轮都会确定一个最终元素
4）持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较
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

