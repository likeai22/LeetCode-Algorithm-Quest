from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new_list = []

        while current:
            new_list.append(current.val)
            current = current.next

        new_list.sort()

        dummy = head

        for node in new_list:
            dummy.val = node
            dummy = dummy.next

        return head
