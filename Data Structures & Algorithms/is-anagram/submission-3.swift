class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        if s.count == t.count {
            var ds: [Character: Int] = [:]
            var dt: [Character: Int] = [:]
            for c in s {
                if ds[c] == nil {
                    ds[c] = 0
                }
                ds[c]! += 1
            }
            for c in t {
                if dt[c] == nil {
                    dt[c] = 0
                }
                dt[c]! += 1
            }
            return ds == dt
        } else {
            return false
        }
    }
}
