class MyHashSet {

    var setp: [Bool] = []
    var setn: [Bool] = []

    init() {

    }

    func add(_ key: Int) {
        if key >= 0 {
            while self.setp.count <= key {
                self.setp.append(false)
            }
            self.setp[key] = true
        } else {
            while self.setn.count < -key {
                self.setn.append(false)
            }
            self.setn[-key-1] = true
        }
    }

    func remove(_ key: Int) {
        if key >= 0 {
            if self.setp.count > key {
                self.setp[key] = false
            }
        } else {
            if self.setn.count > -key - 1 {
                self.setn[-key-1] = false
            }
        }
    }

    func contains(_ key: Int) -> Bool {
        if key >= 0 {
            if self.setp.count > key {
                return self.setp[key]
            }
        } else {
            if self.setn.count > -key - 1 {
                return self.setn[-key-1]
            }
        }
        return false
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * let ret_3: Bool = obj.contains(key)
 */
