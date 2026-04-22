# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        current = head
        while current != None:
            new = ListNode(current.val, new)
            current = current.next
        return new
        