# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = head
        cnt = 1
        while tmp.next is not None:
            cnt += 1
            tmp = tmp.next

        tmp = head
        for _ in range(int(cnt / 2)):
            tmp = tmp.next

        return tmp

class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            if fast.next is None:
                return slow
            else:
                fast = fast.next
        return slow

