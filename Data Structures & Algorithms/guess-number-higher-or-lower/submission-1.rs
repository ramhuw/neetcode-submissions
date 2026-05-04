// The guess API is already defined for you.
// fn guess(num: i64) -> i32:
//     -1 if num is higher than the picked number
//      1 if num is lower than the picked number
//      0 if num is equal to the picked number

impl Solution {
    pub unsafe fn guess_number(n: i64) -> i64 {
        let mut l = 1i128;
        let mut r = n as i128;
        loop {
            let m = (l + r) / 2;
            match unsafe { guess(m as i64) } {
                0 => return m as i64,
                -1 => r = m - 1,
                1 => l = m + 1,
                _ => {}
            }
        }
    }
}
