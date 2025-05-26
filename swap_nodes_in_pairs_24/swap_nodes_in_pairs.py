# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        # setting tmp before loop reduces memory
        tmp = None
        while (curr and curr.next):
            prev = curr
            curr = prev.next
            # swap values
            tmp = prev.val
            prev.val = curr.val
            curr.val = tmp
            # move curr ahead
            curr = curr.next
        
        return head