class Solution {
    func sortArray(_ nums: [Int]) -> [Int] {
        if nums.count == 0 {
            return nums
        } else {
            return self.sortArray(nums.filter { $0 < nums[0] }) + nums.filter { $0 == nums[0] } + self.sortArray(nums.filter { $0 > nums[0] })
        }
    }
}
