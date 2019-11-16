# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # left is included while right is not included
        def _generateTrees(left, right):
            if (left == right):
                return []
            if (left == (right - 1)):
                return [TreeNode(left)]

            trees = []
            for i in range(right - left):
                left_list = _generateTrees(left, left+i)
                right_list = _generateTrees(left+i+1, right)

                if len(left_list) == 0:
                    for j in right_list:
                        root = TreeNode(left + i)
                        root.right = j
                        trees.append(root)
                else:
                    for j in left_list:
                        if len(right_list) != 0:
                            for k in right_list:
                                root = TreeNode(left + i)
                                root.left = j
                                root.right = k
                                trees.append(root)
                        else:
                            root = TreeNode(left + i)
                            root.left = j
                            trees.append(root)

            return trees
        return _generateTrees(1, n + 1)

