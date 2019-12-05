# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 28ms/100%
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None:
            if root2 is None:
                return True
            else:
                return False
        else:
            if root2 is None:
                return False

        if root1.val != root2.val:
            return False

        if self.flipEquiv(root1.left, root2.left):
            return self.flipEquiv(root1.right, root2.right)
        else:
            if self.flipEquiv(root1.left, root2.right):
                return self.flipEquiv(root1.right, root2.left)
            else:
                return False
        return True