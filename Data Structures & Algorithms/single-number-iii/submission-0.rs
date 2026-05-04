impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        let sum = nums.iter().fold(0, |acc, a| acc ^ a);
        let mut i = 0;
        while (1 << i) & sum == 0 {
            i += 1;
        }
        let mask = 1 << i;
        let sum1 = nums.iter().filter(|n| **n & mask != 0).fold(0, |acc, a| acc^a);
        let sum2 = nums.iter().filter(|n| **n & mask == 0).fold(0, |acc, a| acc^a);
        vec![sum1, sum2]
    }
}
