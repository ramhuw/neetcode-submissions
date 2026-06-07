class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        var set: Set<Int> = []
        for n in nums {
            if set.contains(n) {
                return true
            } else {
                set.insert(n)
            }
        }
        return false
    }
}
