# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# using stack!
# 356ms/68.85%
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        pts = head
        nums = []
        while pts is not None:
            nums.append(pts.val)
            pts = pts.next
        stack = []
        answ = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[len(stack)-1]] < nums[i]:
                idx = stack.pop()
                answ[idx] = nums[i]
            stack.append(i)
        return answ


 

