class Solution {
    fun mergeKLists(lists: Array<ListNode?>): ListNode? {
        if (lists.size == 0) {
            return null
        } else if (lists.size == 1) {
            return lists[0]
        } else {
            var list1 = lists[0]
            var list2 = mergeKLists(lists.copyOfRange(1, lists.size))
            var ans: ListNode? = null
            var current = ans
            while (list1 != null || list2 != null) {
                var v: Int
                if (list1 != null && list2 != null) {
                    if (list1.`val` < list2.`val`){
                        v = list1.`val`
                        list1 = list1.next
                    } else {
                        v = list2.`val`
                        list2 = list2.next
                    }
                } else if (list1 == null) {
                    v = list2!!.`val`
                    list2 = list2.next
                } else {
                    v = list1.`val`
                    list1 = list1.next
                }
                if (ans == null) {
                    ans = ListNode(v)
                    current = ans
                } else {
                    current?.next = ListNode(v)
                    current = current?.next
                }
            }
            return ans
        }
    }
}