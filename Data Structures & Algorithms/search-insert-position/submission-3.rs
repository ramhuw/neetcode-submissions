impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let mut l = 0;
        let mut r = nums.len() - 1;
        loop {
            let mid = (l + r) / 2;
            if l + 1 >= r {
                if nums[r] < target {
                    return (r + 1) as i32;
                } else if nums[l] >= target {
                    return l as i32;
                } else {
                    return r as i32;
                }
            }
            if nums[mid] == target {
                return mid as i32;
            }
            
            if nums[mid] > target {
                r = mid;
            } else {
                l = mid;
            }
        }
    }
}
