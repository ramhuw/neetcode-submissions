impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut ans = String::new();
        let mut i = 0;
        let w = strs.iter().map(|s| s.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();
        'outer: while let Some(c) = w[0].get(i) {
            for word in w.clone() {
                if word.get(i) != Some(c) {
                    break 'outer;
                }
            }
            ans.push(*c);
            i += 1;
        }
        ans
    }
}
