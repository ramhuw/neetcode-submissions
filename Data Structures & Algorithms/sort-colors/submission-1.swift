class Solution {
    func sortColors(_ nums: inout [Int]) {
        let n = nums.count
        var i = 0
        while i < n - 1 {
            while i < n - 1 && nums[i] > nums[i + 1] {
                var j = i + 1
                while j > 0 && nums[j-1] > nums[j] {
                    (nums[j], nums[j-1]) = (nums[j-1], nums[j])
                    j -= 1
                }
                i += 1
            }
            i += 1
        }
    }
}
