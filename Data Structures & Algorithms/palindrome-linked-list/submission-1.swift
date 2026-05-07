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
    func isPalindrome(_ head: ListNode?) -> Bool {
        if head == nil || head!.next == nil{
            return true
        } else if head!.next!.next == nil {
            return head!.val == head!.next!.val
        }
        var current = head!.next
        var next = current!.next
        while next!.next != nil {
            current = current!.next
            next = next!.next
        }
        current!.next = nil
        return head!.val == next!.val && self.isPalindrome(head!.next)
    }
}
