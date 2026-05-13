class LinkedList {

    var head: Node? = nil

    func get(_ index: Int) -> Int {
        var i = 0
        var current = self.head
        while i != index {
            if current == nil {
                return -1
            } else {
                current = current!.next
                i += 1
            }
        }
        return current != nil ? current!.val : -1
    }

    func insertHead(_ value: Int) {
        let newHead: Node? = Node(value)
        newHead!.next = self.head
        self.head = newHead
    }

    func insertTail(_ value: Int) {
        if self.head == nil {
            self.head = Node(value)
            return
        } else {
            var current = self.head
            var next = self.head!.next
            while next != nil {
                current = current!.next
                next = next!.next
            }
            let newTail: Node? = Node(value)
            current!.next = newTail
        }
    }

    func remove(_ index: Int) -> Bool {
        if index == 0 {
            if self.head != nil {
                self.head = self.head!.next
                return true
            } else {
                return false
            }
        }
        var i = 0
        var current = self.head
        while i + 1 != index {
            if current == nil || current!.next == nil {
                return false
            } else {
                current = current!.next
                i += 1
            }
        }
        if current == nil || current!.next == nil {
            return false
        } else if current!.next!.next == nil {
            current!.next = nil
        } else {
            current!.next = current!.next!.next
        }
        return true
    }

    func getValues() -> [Int] {
        var result: [Int] = []
        var current = self.head 
        while current != nil {
            result.append(current!.val)
            current = current!.next
        }
        return result
    }
}

class Node {
    var val: Int
    var next: Node? = nil
    init(_ val: Int) {
        self.val = val
    }
}
