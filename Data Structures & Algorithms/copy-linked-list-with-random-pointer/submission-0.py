"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        p1 = head
        ans = Node(head.val, None, None)
        p2 = ans
        m = {p1: p2}
        while p1.next != None:
            p1 = p1.next
            new = Node(p1.val, None, None)
            p2.next = new
            p2 = new
            m[p1] = p2
        
        p1 = head
        p2 = ans
        while p1 != None:
            if p1.random != None:
                p2.random = m[p1.random]
            p1 = p1.next
            p2 = p2.next
        return ans
