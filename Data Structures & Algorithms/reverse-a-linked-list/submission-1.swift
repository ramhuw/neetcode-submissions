/**
 * Definition for singly-linked list.
 * class ListNode {
 *     var val: Int
 *     var next: ListNode?
 *     init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        if head == nil || head!.next == nil {
            return head
        } else {
            let newHead = self.reverseList(head!.next)
            var current = newHead
            while current!.next != nil {
                current = current!.next
            }
            current!.next = ListNode(head!.val)
            return newHead
        }
    }
}
