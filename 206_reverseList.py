from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def display(self):
        if self.head == None:
            print("List Empty")
            return
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next

    def reverseList(self):
        curr, prev = self.head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        self.head = prev
        return self.head


# Definition for singly-linked list.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        head = prev
        return head


if __name__ == "__main__":
    a_list = LinkedList()
    for i in range(1, 6):
        a_list.append(i)
    a_list.display()
    print("*" * 20)
    a_list.reverseList()
    a_list.display()
