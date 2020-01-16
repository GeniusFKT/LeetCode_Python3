# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import random
# 84ms/93.84%
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.length = 0
        while head is not None:
            self.length += 1
            head = head.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        counter = self.length
        ptr = self.head
        while True:
            if random.random() * counter <= 1:
                return ptr.val
            counter -= 1
            ptr = ptr.next

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()