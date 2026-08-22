"""
deque -- 双端队列
支持从两端快速添加和删除元素，时间复杂度O(1)，比list在头部操作时更高效
"""

from collections import deque

dq = deque([1, 2, 3])
dq.append(4)    # 右侧添加
dq.appendleft(0)  # 左侧添加
print(dq)

dq.pop()   # 删除右侧
dq.popleft()   # 删除左侧（比 list.pop(0) 快得多）
print(dq)
