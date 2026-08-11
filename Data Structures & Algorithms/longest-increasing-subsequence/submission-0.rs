impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut d: Vec<i32> = vec![-1001];
        for x in nums {
            let mut left: usize = 0;
            let mut right: usize = d.len();
            while left + 1 < right {
                let middle = (left + right) / 2;
                if d[middle] < x {
                    left = middle;
                } else {
                    right = middle;
                }
            }
            if right == d.len() {
                d.push(x);
            } else {
                d[right] = x;
            }
        }
        d.len() as i32 - 1
    }
}
