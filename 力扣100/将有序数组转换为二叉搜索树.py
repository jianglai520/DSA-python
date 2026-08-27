from typing import Optional, List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def dfs(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        root.left = dfs(left, mid - 1)
        root.right = dfs(mid + 1, right)

        return root
    return dfs(0, len(nums) - 1)