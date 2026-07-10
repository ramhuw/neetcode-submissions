class Solution {
    fun islandPerimeter(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var ans = 0
        for (i in 0..<m) {
            for (j in 0..<n) {
                if (grid[i][j] == 1) {
                    if (i == 0 || grid[i-1][j] == 0) {
                        ans += 1
                    }
                    if (j == 0 || grid[i][j-1] == 0) {
                        ans += 1
                    }
                    if (i == m - 1 || grid[i+1][j] == 0) {
                        ans += 1
                    }
                    if (j == n - 1 || grid[i][j+1] == 0) {
                        ans += 1
                    }
                }
            }
        }
        return ans
    }
}