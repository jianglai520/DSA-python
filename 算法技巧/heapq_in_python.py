"""
先说一下什么是堆？
堆就是一种特殊的完全二叉树
小顶堆：每个父节点 <= 子节点，所以堆顶是最小值
大顶堆：每个父节点 >= 子节点，所以堆顶是最大值

那么知道了这些基础，你就知道了堆常见的用户就是：快速拿到一堆数据里的最小值或最大值

heapq就是python标准库里面的一个模块，全称是 heap queue（堆排列），专门用来实现优先队列
注意：python中的heapq只提供小顶堆，没有大顶堆。它把普通列表当作堆来操作，所有函数都是围绕这个列表的
"""

import heapq

nums = []

# heappush(heap, item) -- 插入元素
heapq.heappush(nums, 5)
heapq.heappush(nums, 1)
heapq.heappush(nums, 8)
print(nums)

# heappop(heap) -- 弹出并返回最小值
print(heapq.heappop(nums))
print(nums)

# heap[0] -- 查看堆顶（最小值），不弹出
print(nums[0])

# heapify(list) -- 把普通列表原地变成堆
arr = [5, 1, 8, 3, 9, 2]
heapq.heapify(arr)
print(arr[0])
print(arr)