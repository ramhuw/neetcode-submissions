class Deque {

    private var left: DoubleNode? = null
    private var right: DoubleNode? = null

    fun isEmpty(): Boolean {
        return left == null
    }

    fun append(value: Int) {
        val newNode = DoubleNode(value)
        if (isEmpty()) {
            left = newNode
            right = newNode
        } else {
            right!!.right = newNode
            newNode.left = right
            right = newNode
        }
    }

    fun appendleft(value: Int) {
        val newNode = DoubleNode(value)
        if (isEmpty()) {
            left = newNode
            right = newNode
        } else {
            left!!.left = newNode
            newNode.right = left
            left = newNode
        }
    }

    fun pop(): Int {
        val ans = right?.value ?: -1
        if (left == right) {
            left = null
            right = null
        } else {
            right = right?.left
            right!!.right = null
        }
        return ans
    }

    fun popleft(): Int {
        val ans = left?.value ?: -1
        if (left == right) {
            left = null
            right = null
        } else {
            left = left?.right
            left!!.left = null
        }
        return ans
    }
}


private class DoubleNode(val value: Int) {
    var left: DoubleNode? = null
    var right: DoubleNode? = null
}