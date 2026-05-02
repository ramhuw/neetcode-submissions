impl Solution {
    pub fn score_of_string(s: String) -> i32 {
        let a = s.chars().map(|c| c as u32).collect::<Vec<u32>>();
        let mut ans = 0;
        for i in 0..(a.len() - 1) {
            ans += if a[i + 1] > a[i] {a[i + 1] - a[i]} else {a[i] - a[i + 1]};
        }
        ans as i32
    }
}
