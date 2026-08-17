class Node(val value: Int) {
    var next: Node? = null
}

class LinkedList {

    var head: Node? = null

    fun get(index: Int): Int {
        var cur = head
        var i = 0
        while (i != index) {
            if (cur == null) {
                return -1
            }
            cur = cur.next
            i += 1
        }
        return cur?.value ?: -1
    }

    fun insertHead(value: Int) {
        val newHead = Node(value)
        newHead.next = head
        head = newHead
    }

    fun insertTail(value: Int) {
        val newTail = Node(value)
        if (head == null) {
            head = newTail
        } else {
            var cur = head
            while (cur?.next != null) {
                cur = cur.next
            }
            cur!!.next = newTail
        }
    }

    fun remove(index: Int): Boolean {
        if (index == 0) {
            if (head == null) {
                return false
            } else {
                head = head?.next
                return true
            }
        } else {
            var cur = head
            var i = 0
            while (i + 1 != index) {
                if (cur == null) {
                    return false
                }
                cur = cur.next
                i += 1
            }
            if (cur?.next == null) {
                return false
            }
            cur.next = cur.next?.next
            return true
        }
    }

    fun getValues(): List<Int> {
        val values: MutableList<Int> = mutableListOf()
        var cur = head
        while (cur != null) {
            values.addLast(cur.value)
            cur = cur.next
        }
        return values
    }
}
