from operator import is_not_none
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    count = 0
    result = None

    def inorder(node):
        nonlocal count, result

        if not node or result is not None:
            return

        inorder(node.left)

        count += 1
        if count == k:
            result = node.val
            return

        inorder(node.right)
    inorder(root)
    return result