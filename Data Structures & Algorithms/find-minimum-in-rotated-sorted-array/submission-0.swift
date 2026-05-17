class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var l = 0
        var r = nums.count - 1
        while true {
            if l == r {
                return min(nums[l], nums[0])
            }
            let mid = (l + r) / 2
            if nums[mid] < nums[0] + mid {
                r = mid
            } else {
                l = mid + 1
            }
        }
    }
}
