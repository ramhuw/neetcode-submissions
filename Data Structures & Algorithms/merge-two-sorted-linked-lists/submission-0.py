# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start: Optional[ListNode] = None
        current: Optional[ListNode] = None
        while True:
            nn = None
            if list1 != None:
                if list2 == None or list1.val <= list2.val:
                    nn = ListNode(list1.val, None)
                    list1 = list1.next
                else:
                    nn = ListNode(list2.val, None)
                    list2 = list2.next
            elif list2 != None:
                nn = ListNode(list2.val, None)
                list2 = list2.next
            else:
                break
            if start == None or current == None:
                start = nn
                current = start
            else:
                current.next = nn
                current = current.next
        return start