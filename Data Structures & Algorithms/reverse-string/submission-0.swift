class Solution {
    func reverseString(_ s: inout [Character]) {
        let n = s.count
        for i in 0..<(n/2) {
            (s[i], s[n - 1 - i]) = (s[n - 1 - i], s[i])
        }
    }
}
