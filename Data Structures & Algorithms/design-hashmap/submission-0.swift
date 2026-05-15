class MyHashMap {

    var map: [Int?] = []

    init() {

    }

    func put(_ key: Int, _ value: Int) {
        while key >= self.map.count {
            self.map.append(nil)
        }
        self.map[key] = value
    }

    func get(_ key: Int) -> Int {
        if key >= self.map.count || self.map[key] == nil {
            return -1
        } else {
            return self.map[key]!
        }
    }

    func remove(_ key: Int) {
        if key < self.map.count {
            self.map[key] = nil
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * let obj = MyHashMap()
 * obj.put(key, value)
 * let ret_2: Int = obj.get(key)
 * obj.remove(key)
 */
