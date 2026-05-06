impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut ans = vec![vec![0; n]; m];
        for i in 0..m {
            for j in 0..n {
                if obstacle_grid[i][j] == 0 {
                    if i == 0 && j == 0 {
                        ans[i][j] = 1;
                    }
                    if i > 0 {
                        ans[i][j] += ans[i - 1][j]
                    }
                    if j > 0 {
                        ans[i][j] += ans[i][j - 1]
                    }
                }
            }
        }
        ans[m-1][n-1]
    }
}
