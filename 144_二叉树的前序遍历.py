# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 36ms/91.69%
class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def _preorderTraversal(root):
            if root is None:
                return
            else:
                self.result.append(root.val)
                _preorderTraversal(root.left)
                _preorderTraversal(root.right)
        _preorderTraversal(root)
        return self.result
