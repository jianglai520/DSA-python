from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = Nonefix):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    if not root:
        return 0

    def dfs(node, cur_sum):
        if not node:
            return 0

        cur_sum += node.val
        count = 1 if cur_sum == targetSum else 0
        count += dfs(node.left, cur_sum)
        count += dfs(node.right, cur_sum)

        return count

    return (dfs(root, 0)) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)