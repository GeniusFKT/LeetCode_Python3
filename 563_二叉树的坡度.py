# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 56ms/100%
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        # return sum and tilt simutaneously
        def _findTilt(root):
            if root.left is None:
                if root.right is None:
                    return root.val, 0
                else:
                    right_sum, right_tilt = _findTilt(root.right)
                    return root.val + right_sum, abs(right_sum) + right_tilt
            if root.right is None:
                left_sum, left_tilt = _findTilt(root.left)
                return root.val + left_sum, abs(left_sum) + left_tilt

            left_sum, left_tilt = _findTilt(root.left)
            right_sum, right_tilt = _findTilt(root.right)
            return left_sum + root.val + right_sum, abs(right_sum - left_sum) + left_tilt + right_tilt

        if root is None:
            return 0
        else:
            return _findTilt(root)[1]

# simplify version
# 68ms/91.45%
class Solution1:
    def findTilt(self, root: TreeNode) -> int:
        # return sum and tilt simutaneously
        def _findTilt(root):
            if root is None:
                return 0, 0

            left_sum, left_tilt = _findTilt(root.left)
            right_sum, right_tilt = _findTilt(root.right)
            return left_sum + root.val + right_sum, abs(right_sum - left_sum) + left_tilt + right_tilt

        return _findTilt(root)[1]