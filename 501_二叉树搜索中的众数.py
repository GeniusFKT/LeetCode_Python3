# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 112ms/18.06%
class Solution:
    def __init__(self):
        self.max_list = []
        self.max_times = 0
        self.count = -1
        self.num = -1

    def findMode(self, root: TreeNode) -> List[int]:
        self._traverse(root)
        self._update()
        return self.max_list

    def _traverse(self, root):
        if root is None:
            return
        self._traverse(root.left)
        if root.val == self.num:
            self.count += 1
        else:
            self._update()
            self.count = 1
            self.num = root.val
        self._traverse(root.right)

    def _update(self):
        if self.max_times < self.count:
            self.max_times = self.count
            self.max_list = [self.num]
        elif self.max_times == self.count:
            self.max_list.append(self.num)
