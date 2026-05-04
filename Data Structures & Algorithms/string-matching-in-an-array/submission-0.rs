impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        let mut ans = Vec::new();
        for word in &words {
            for test in &words {
                if word != test && test.contains(word) {
                    ans.push(word.clone());
                    break;
                }
            }
        }
        ans
    }
}
