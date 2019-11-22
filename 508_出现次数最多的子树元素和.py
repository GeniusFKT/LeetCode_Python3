# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 64ms/83.33%
# recursive
class Solution:
    def __init__(self):
        self.count = {}

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self._findFrequentTreeSum(root)
        maximum = max(self.count.values())
        ans = []
        for i in self.count.keys():
            if self.count[i] == maximum:
                ans.append(i)

        return ans

    def _findFrequentTreeSum(self, root):
        if root is None:
            return 0
        left_sum = self._findFrequentTreeSum(root.left)
        right_sum = self._findFrequentTreeSum(root.right)

        total_sum = left_sum + right_sum + root.val
        if self.count.get(total_sum) is None:
            self.count[total_sum] = 1
        else:
            self.count[total_sum] += 1
        return total_sum