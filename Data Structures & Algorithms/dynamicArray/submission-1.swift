class DynamicArray {

    private var head: Node?
    private var capacity: Int

    init(_ capacity: Int) {
        self.capacity = capacity
    }

    func get(_ i: Int) -> Int {
        var counter = 0
        var current = head
        while counter < i {
            current = current!.getNext()
            counter += 1
        }
        return current!.getVal()
    }

    func set(_ i: Int, _ n: Int) {
        var counter = 0
        var current = head
        while counter < i {
            current = current!.getNext()
            counter += 1
        }
        current!.setVal(n)
    }

    func pushback(_ n: Int) {
        if self.getSize() >= self.getCapacity() {
            self.resize()
        }
        if head == nil {
            head = Node(n)
        } else {
            var current = head
            var next = current!.getNext()
            while next != nil {
                current = current!.getNext()
                next = next!.getNext()
            }
            current!.setNext(Node(n))
        }
        
    }

    func popback() -> Int {
        var current = self.head
        var next = head!.getNext()
        if next == nil {
            self.head = nil
            return current!.getVal()
        } else {
            var nextNext = next!.getNext()
            while nextNext != nil {
                current = current!.getNext()
                next = next!.getNext()
                nextNext = nextNext!.getNext()
            }
            current!.setNext(nil)
            return next!.getVal()
        }

    }

    private func resize() {
        self.capacity *= 2
    }

    func getSize() -> Int {
        var counter = 0
        var current = head
        while current != nil {
            counter += 1
            current = current!.getNext()
        }
        return counter
    }

    func getCapacity() -> Int {
        return self.capacity
    }
}

class Node {

    private var val: Int
    private var next: Node?

    init(_ val: Int) {
        self.val = val
    }

    func getNext() -> Node? {
        return self.next
    }

    func getVal() -> Int {
        return self.val
    }

    func setNext(_ next: Node?) {
        self.next = next
    }

    func setVal(_ val: Int) {
        self.val = val
    }
}