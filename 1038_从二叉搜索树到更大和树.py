# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 后序遍历
# 40ms/91.06%
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def _bstToGst(root, s):
            if root is None:
                return s
            right_sum = _bstToGst(root.right, s)
            root.val += right_sum
            return _bstToGst(root.left, root.val)
        _bstToGst(root, 0)
        return root