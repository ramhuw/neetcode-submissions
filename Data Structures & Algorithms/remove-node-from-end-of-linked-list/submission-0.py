# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        current = head
        while current != None:
            current = current.next
            l += 1
        n = l - n
        if head == None:
            return head
        elif n == 0:
            return head.next
        left = head
        counter = 1
        while counter < n:
            if left.next == None:
                return head
            left = left.next
            counter += 1
        if left.next == None:
            return head
        left.next = left.next.next
        return head

