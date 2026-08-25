# 定义二叉树
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val  = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    root = TreeNode(1)  # 根节点
    root.left = TreeNode(2)   # 左孩子
    root.right = TreeNode(3)  # 右孩子
