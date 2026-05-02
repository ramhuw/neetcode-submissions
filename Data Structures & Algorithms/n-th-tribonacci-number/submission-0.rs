impl Solution {
    pub fn tribonacci(n: i32) -> i32 {
        let mut stack = vec![0, 1, 1];
        for i in 3..=n as usize {
            stack.push(stack[i-1] + stack[i-2] + stack[i-3]);
        }
        stack[n as usize]
    }
}
