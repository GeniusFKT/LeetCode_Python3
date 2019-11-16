# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        if fast is None:
            return False
        while fast.next is not None:
            fast = fast.next
            if fast == slow:
                return True
            slow = slow.next
            if fast.next is None:
                return False
            else:
                fast = fast.next
        return False