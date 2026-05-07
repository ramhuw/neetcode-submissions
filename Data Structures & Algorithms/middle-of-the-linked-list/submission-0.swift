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
    func middleNode(_ head: ListNode?) -> ListNode? {
        var counter = 0
        var current = head
        while current != nil {
            current = current!.next
            counter += 1
        }
        current = head
        var mid = counter / 2
        var i = 0
        while i < mid {
            current = current!.next
            i += 1
        }
        return current
    }
}
