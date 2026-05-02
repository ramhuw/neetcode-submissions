impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut ans = vec![vec![1]];
        for i in 1..(num_rows as usize) {
            let mut row = vec![1];
            for j in 1..i {
                row.push(ans[i-1][j-1] + ans[i-1][j]);
            }
            row.push(1);
            ans.push(row);
        }
        ans
    }
}
