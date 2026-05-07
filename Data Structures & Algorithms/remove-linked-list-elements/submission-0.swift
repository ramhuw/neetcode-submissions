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
    func removeElements(_ head: ListNode?, _ val: Int) -> ListNode? {
        if head == nil {
            return head
        }
        if head!.val == val {
            return self.removeElements(head!.next, val)
        } else {
            head!.next = self.removeElements(head!.next, val)
            return head
        }
    }
}
