impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        nums.iter().map(|n| n.to_string()).collect::<Vec<String>>().join("").split(|c| c != '1').max_by_key(|&word| word.len()).unwrap().len() as i32
    }
}
