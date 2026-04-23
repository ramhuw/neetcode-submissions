impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let mut s: Vec<i32> = vec![cost[0], cost[1]];
        let n = cost.len();
        for i in 2..n {
            s.push(cost[i] + s[i - 1].min(s[i - 2]));
        }
        s[n-1].min(s[n-2])
    }
}
