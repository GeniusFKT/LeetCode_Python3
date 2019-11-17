# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 40ms/96.35%
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        if root.left is None:
            self.flatten(root.right)
            return
        self.flatten(root.left)
        self.flatten(root.right)
        pts = root.left
        while pts.right is not None:
            pts = pts.right

        tmp = root.right
        root.right = root.left
        pts.right = tmp
        root.left = None