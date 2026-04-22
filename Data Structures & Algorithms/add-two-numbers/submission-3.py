# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        a = 0
        b = 0
        if l1 != None:
            a = l1.val
            l1 = l1.next
        if l2 != None:
            b = l2.val
            l2 = l2.next
        head = ListNode((a + b) % 10, None)
        carry = (a + b) // 10
        ans = head
        while l1 != None or l2 != None:
            a = 0
            b = 0
            if l1 != None:
                a = l1.val
                l1 = l1.next
            if l2 != None:
                b = l2.val
                l2 = l2.next
            new_node = ListNode((a + b + carry) % 10, None)
            carry = (a + b + carry) // 10
            ans.next = new_node
            ans = ans.next
        if carry != 0:
            new_node = ListNode(carry, None)
            ans.next = new_node
        return head
