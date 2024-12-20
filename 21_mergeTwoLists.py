from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        new_list = ListNode()
        head = new_list

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next

            head = head.next
        if list1 == None and list2 != None:
            head.next = list2
        if list2 == None and list1 != None:
            head.next = list1

        return new_list.next
