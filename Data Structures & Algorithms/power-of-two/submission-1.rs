impl Solution {
    pub fn is_power_of_two(n: i32) -> bool {
        let mut n = n;
        if n <= 0 {
            return false;
        }
        while n % 2 == 0 {
            n /= 2;
        }
        if n == 1 {
            return true;
        } else {
            false
        }
    }
}
