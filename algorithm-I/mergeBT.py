from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_Trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

    def dfs(node1, node2):
        if node1 and node2:
            root = TreeNode(node1.val + node2.val)
            root.left = dfs(node1.left, node2.left)
            root.right = dfs(node1.right, node2.right)
            return root
        else: return node1 or node2
    return dfs(root1, root2)
    