from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)

    root.left = buildTree(
        preorder[1: 1 + mid],
        inorder[:mid]
    )

    root.right = buildTree(
        preorder[1 + mid:],
        inorder[mid + 1:]
    )

    return root