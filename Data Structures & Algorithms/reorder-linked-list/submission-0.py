# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None:
            return
        elif head.next == None:
            return
        left = head.next
        right_current = head.next
        right = ListNode(right_current.val, None)
        counter = 1
        while right_current.next != None:
            right_current = right_current.next
            right = ListNode(right_current.val, right)
            counter += 1
        current = head
        flag = True
        while counter > 0:
            if flag:
                current.next = ListNode(right.val, None)
                right = right.next
            else:
                current.next = ListNode(left.val)
                left = left.next
            counter -= 1
            current = current.next
            flag = not flag

