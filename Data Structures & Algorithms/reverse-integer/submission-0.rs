impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let flag = if x >= 0 {1} else {-1};
        let mut s: Vec<i32> = Vec::new();
        let mut n = x.abs();
        while n != 0 {
            s.push(flag * (n % 10));
            n /= 10;
        }
        let mut ans: i32 = 0;
        let mut bit: i32 = 1;
        while let Some(d) = s.pop() {
            let f = match d.checked_mul(bit) {
                Some(m) => m,
                None => return 0,
            };
            match ans.checked_add(d*bit) {
                Some(a) => ans = a,
                None => return 0,
            }
            match bit.checked_mul(10) {
                Some(b) => bit = b,
                None => {
                    if s.len() > 0 {
                        return 0;
                    }
                }
            }
        }
        return ans;

    }
}
