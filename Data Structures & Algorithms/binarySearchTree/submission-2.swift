class TreeMap {

    var head: Node? = nil

    func insert(_ key: Int, _ value: Int) {
        if self.head == nil {
            self.head = Node(key, value)
            return 
        }
        var current = self.head
        while true {
            if current!.key == key {
                current!.value = value
                break
            } else if current!.key > key {
                if current!.left == nil {
                    current!.left = Node(key, value)
                    return
                } else {
                    current = current!.left
                }
            } else {
                if current!.right == nil {
                    current!.right = Node(key, value)
                    return
                } else {
                    current = current!.right
                }
            }
        }
    }

    func get(_ key: Int) -> Int {
        var current = self.head
        while current != nil {
            if current!.key == key {
                return current!.value
            } else if current!.key > key {
                current = current!.left
            } else {
                current = current!.right
            }
        }
        return -1
    }

    func getMin() -> Int {
        if self.head == nil {
            return -1
        } else {
            var current = self.head
            while current!.left != nil {
                current = current!.left
            }
            return current!.value
        }
    }

    func getMax() -> Int {
        if self.head == nil {
            return -1
        } else {
            var current = self.head
            while current!.right != nil {
                current = current!.right
            }
            return current!.value
        }
    }

    func remove(_ key: Int) {
        if self.head == nil { return }
        
        // Helper to find node and parent
        var parent: Node? = nil
        var curr = self.head
        while curr != nil && curr!.key != key {
            parent = curr
            curr = key < curr!.key ? curr!.left : curr!.right
        }
        
        if curr == nil { return } // Key not found

        if self.head!.key == key {
            if self.head!.left != nil {
                var current = self.head!.left
                while current!.right != nil {
                    current = current!.right
                }
                current!.right = self.head!.right
                self.head = self.head!.left
            } else {
                self.head = self.head!.right
            } 
        } else {
                var current = parent
                var next = curr
                
                if current!.left === next {
                    if next!.left != nil {
                        var search = next!.left
                        while search!.right != nil {
                            search = search!.right
                        }
                        search!.right = next!.right
                        current!.left = next!.left
                    } else {
                        current!.left = next!.right
                    }
                } else {
                    if next!.left != nil {
                        var search = next!.left
                        while search!.right != nil {
                            search = search!.right
                        }
                        search!.right = next!.right
                        current!.right = next!.left
                    } else {
                        current!.right = next!.right
                    }
                }
        }
    }

    func getInorderKeys() -> [Int] {
        return getKeys(self.head)
    }
}

class Node {
    var key: Int
    var value: Int
    var left: Node? = nil
    var right: Node? = nil
    init(_ key: Int, _ value: Int) {
        self.key = key
        self.value = value
    }
    
}

func getKeys(_ node: Node?) -> [Int] {
    if node == nil {
        return []
    } else {
        return getKeys(node!.left) + [node!.key] + getKeys(node!.right)
    }
}