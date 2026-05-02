impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let mut m = -1;
        let mut arr = arr;
        let mut ans = Vec::new();
        while let Some(n) = arr.pop() {
            ans.push(m);
            m = m.max(n);
        }
        ans.reverse();
        ans
    }
}
