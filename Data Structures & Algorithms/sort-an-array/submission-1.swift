class Solution {
    func sortArray(_ nums: [Int]) -> [Int] {
        if nums.count == 0 {
            return nums
        } else {
            return self.sortArray(nums[1...].filter { $0 <= nums[0] }) + [nums[0]] + self.sortArray(nums[1...].filter { $0 > nums[0] })
        }
    }
}
