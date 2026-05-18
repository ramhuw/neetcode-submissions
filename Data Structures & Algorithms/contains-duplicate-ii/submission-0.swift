class Solution {
    func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
        var table: Set<Int> = Set()
        let n = nums.count
        for i in 0...k {
            if i >= n {
                break
            }
            if table.contains(nums[i]) {
                return true
            } else {
                table.insert(nums[i])
            }
        }
        if k + 1 >= n {
            return false
        }
        for i in 1..<(n - k) {
            table.remove(nums[i-1])
            if table.contains(nums[k + i]) {
                return true
            } else {
                table.insert(nums[k + i])
            }
        }
        return false
    }
}
