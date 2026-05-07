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
    func hasCycle(_ head: ListNode?) -> Bool {
        if head == nil || head!.next == nil || head!.next!.next == nil {
            return false
        } else {
            var slow = head!.next
            var fast = head!.next!.next
            while fast != nil && slow != nil {
                if fast === slow {
                    return true
                } else {
                    if fast!.next == nil {
                        return false
                    } else {
                        fast = fast!.next!.next
                        slow = slow!.next
                    }
                }
            }
            return false
        }
    }
}
