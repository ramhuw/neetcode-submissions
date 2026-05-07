class Solution {
    func subsetXORSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<(1 << n) {
            var temp = 0
            for j in 0...n {
                if (1 << j) & i != 0 {
                    temp ^= nums[j]
                }
            }
            ans += temp
        }
        return ans
    }
}
