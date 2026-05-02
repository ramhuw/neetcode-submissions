class Solution {
    func diagonalSum(_ mat: [[Int]]) -> Int {
        let n = mat.count
        var ans = 0
        for i in 0..<n {
            ans += mat[i][i]
            if i != n - i - 1 {
                ans += mat[i][n-i-1]
            }
        }
        return ans
    }
}
