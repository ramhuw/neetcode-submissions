impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let mut set: HashSet<i32> = HashSet::new();
        for n in nums {
            if set.contains(&n) {
                return true;
            } else {
                set.insert(n);
            }
        }
        return false;
    }
}
