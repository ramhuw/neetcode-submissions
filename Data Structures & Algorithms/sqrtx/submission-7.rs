impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        let x = x as i128;
        if x <= 1 {
            return x as i32;
        } else if x <= 3 {
            return 1;
        } 
        let mut l = 2;
        let mut r = x / 2;
        loop {
            if l + 1 >= r {
                if r * r == x {
                    return r as i32;
                } else {
                    return l as i32;
                }
            }
            let m = (l + r)/2;
            if m * m < x {
                l = m;
            } else if m * m > x {
                r = m;
            } else {
                return m as i32;
            }
        }
    }
}
