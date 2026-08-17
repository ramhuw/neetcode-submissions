class TreeMap {

    var root: TreeNode? = null

    fun insert(key: Int, value: Int) {
        if (root == null) {
            root = TreeNode(key, value)
        } else {
            var cur = root
            while (cur!!.key < key && cur.right != null || cur.key > key && cur.left != null) {
                if (cur.key < key) {
                    cur = cur.right
                } else {
                    cur = cur.left
                }
            }
            if (cur.key == key) {
                cur.value = value
            } else {
                val newNode = TreeNode(key, value)
                if (cur.key < key) {
                    cur.right = newNode
                } else {
                    cur.left = newNode
                }
            }
        }
    }

    fun get(key: Int): Int {
        var cur = root
        while (cur != null && cur.key != key) {
            if (cur.key < key) {
                cur = cur.right
            } else {
                cur = cur.left
            }
        }
        if (cur == null) {
            return -1
        } else {
            return cur.value
        }
    }

    fun getMin(): Int {
        if (root == null) {
            return -1
        }
        var cur = root
        while (cur?.left != null) {
            cur = cur.left
        }
        return cur!!.value
    }

    fun getMax(): Int {
        if (root == null) {
            return -1
        }
        var cur = root
        while (cur?.right != null) {
            cur = cur.right
        }
        return cur!!.value
    }

    fun remove(key: Int) {
        var parent: TreeNode? = null
        var child = root
        while (child != null && child.key != key) {
            parent = child
            if (child.key < key) {
                child = child.right
            } else {
                child = child.left
            }
        }
        if (child == null) {
            return
        }
        val left = child.left
        val right = child.right
        val connect = if (left != null) { left } else { right }
        if (left != null && right != null) {
            var cur = left
            while (cur?.right != null) {
                cur = cur.right
            }
            cur!!.right = right
        }
        if (parent != null) {
            if (key < parent.key) {
                parent.left = connect
            } else {
                parent.right = connect
            }
        } else {
            root = connect
        }
    }

    fun getInorderKeys(): List<Int> {
        val visited: MutableSet<TreeNode> = mutableSetOf()
        val searches: MutableList<TreeNode> = mutableListOf()
        val ans: MutableList<Int> = mutableListOf()
        root?.let { searches.add(it) }
        while (searches.isNotEmpty()) {
            val node = searches.removeLast()
            if (node in visited) {
                ans.add(node.key)
                node.right?.let { searches.add(it) }
            } else {
                searches.add(node)
                node.left?.let { searches.add(it) }
                visited.add(node)
            }
        }
        return ans
    }
}

class TreeNode(val key: Int, var value: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}