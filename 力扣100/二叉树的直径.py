from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    max_diameter = 0

    def get_height(node):
        if not node:
            return 0

        left_height = get_height(node.left)
        right_height = get_height(node.right)

        max_diameter =  max(max_diameter, left_height + right_height)

        return 1 + max(left_height, right_height)
    get_height(root)
    return max_diameter