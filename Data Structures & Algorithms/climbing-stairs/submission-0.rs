impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut s: Vec<i32> = Vec::new();
        s.push(1);
        for i in 1..=n as usize {
            let mut step = 0;
            if i > 1 {
                step += s[i - 2];
            }
            step += s[i - 1];
            s.push(step);
        }
        s[n as usize]
    }
}
