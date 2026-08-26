"""
维度	                DFS（深度优先）	            BFS（广度优先）
遍历策略	            一条路走到黑，不撞南墙不回头	    层层推进，像水波一样扩散
数据结构	            栈（递归调用栈）	            队列
遍历顺序	            纵向深入	                    横向扩展
空间消耗	            O(树的高度)	                O(树的宽度)
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    depth = 0
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.appendd(node.right)

        depth += 1

    return depth

