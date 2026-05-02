class Solution {
    func getConcatenation(_ nums: [Int]) -> [Int] {
        return Array(repeating: nums, count: 2).flatMap { $0 }
    }
}
