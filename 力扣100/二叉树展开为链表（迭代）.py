from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    cur = root
    while cur:
        if cur.left:
            pre = cur.left
            while pre.right:
                pre = pre.right

            pre.right = cur.right

            cur.right = cur.left
            cur.left = None
        cur = cur.right
