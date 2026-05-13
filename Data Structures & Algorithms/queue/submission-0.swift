class Deque {

    var l: Node? = nil
    var r: Node? = nil

    func isEmpty() -> Bool {
        self.l == nil
    }

    func append(_ value: Int) {
        var newNode: Node? = Node(value)
        newNode!.left = self.r
        if self.isEmpty() {
            self.l = newNode
            self.r = newNode
        } else {
            self.r!.right = newNode
            self.r = newNode
        }
    }

    func appendleft(_ value: Int) {
        var newNode: Node? = Node(value)
        newNode!.right = self.l
        if self.isEmpty() {
            self.l = newNode
            self.r = newNode
        } else {
            self.l!.left = newNode
            self.l = newNode
        }
    }

    func pop() -> Int {
        if self.isEmpty() {
            return -1
        } else if self.l === self.r {
            let ans = self.l!.val
            self.l = nil
            self.r = nil
            return ans
        } else {
            let ans = self.r!.val
            self.r = self.r!.left
            self.r!.right = nil
            return ans
        }
    }

    func popleft() -> Int {
        if self.isEmpty() {
            return -1
        } else if self.l === self.r {
            let ans = self.l!.val
            self.l = nil
            self.r = nil
            return ans
        } else {
            let ans = self.l!.val
            self.l = self.l!.right
            self.l!.left = nil
            return ans
        }
    }
}

class Node {
    var val: Int
    var left: Node? = nil
    var right: Node? = nil
    init(_ val: Int) {
        self.val = val
    }
}

