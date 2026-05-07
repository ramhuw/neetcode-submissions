class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        nums.sorted().reversed()[nums.count/2]
    }
}
