class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        var ans = grid
        let m = grid.count
        let n = grid[0].count
        for i in 0..<m {
            for j in 0..<n {
                if i > 0 && j > 0 {
                    ans[i][j] += min(ans[i - 1][j], ans[i][j - 1])
                } else if i > 0 {
                    ans[i][j] += ans[i - 1][j]
                } else if j > 0 {
                    ans[i][j] += ans[i][j - 1]
                }
            }
        }
        return ans[m-1][n-1]
    }
}
