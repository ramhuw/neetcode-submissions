/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

extension ListNode: Hashable {
    static public func == (lhs: ListNode, rhs: ListNode) ->Bool {
        lhs === rhs
    }

    public func hash(into hasher: inout Hasher) {
        hasher.combine(ObjectIdentifier(self))
    }
}

class Solution {
    func getIntersectionNode(_ headA: ListNode?, _ headB: ListNode?) -> ListNode? {
        var sa = Set<ListNode>()
        var currentA = headA
        var currentB = headB
        while currentA != nil {
            sa.insert(currentA!)
            currentA = currentA!.next
        }
        while currentB != nil {
            if sa.contains(currentB!) {
                return currentB
            }
            currentB = currentB!.next
        }
        return nil
    }
}
