class HashTable {

    var table: Dictionary<Int, Int>
    var capacity: Int

    init(_ capacity: Int) {
        self.table = Dictionary()
        self.capacity = capacity
    }

    func insert(_ key: Int, _ value: Int) {
        self.table[key] = value
        if self.table.count * 2 >= self.capacity {
            self.resize()
        }
    }

    func get(_ key: Int) -> Int {
        if self.table[key] == nil {
            return -1
        } else {
            return self.table[key]!
        }
    }

    func remove(_ key: Int) -> Bool {
        if self.table[key] == nil {
            return false
        } else {
            self.table[key] = nil
            return true
        }
    }

    func getSize() -> Int {
        return self.table.count
    }

    func getCapacity() -> Int {
        return self.capacity
    }

    func resize() {
        self.capacity *= 2
    }
}
