class Solution {
    func hasDuplicate(_ nums: [Int]) -> Bool {
        var m: [Int: Int] = [:]
        for num in nums {
            if m[num] == nil {
                m[num] = 0
            }
            m[num] = m[num]! + 1
            if m[num]! > 1 {
                return true
            }
        }
        return false
    }
}
