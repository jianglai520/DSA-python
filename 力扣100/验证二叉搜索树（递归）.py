from typing import Optional

class TreeNode:
    def __init(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def helper(node, lower, upper):
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        left_valid = helper(node.left, lower, node.val)

        right_valid = helper(node.right, node.val, upper)

        return left_valid and right_valid

    return helper(root, float('-inf'), float('inf'))