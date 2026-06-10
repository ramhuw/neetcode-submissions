impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let ss = s.to_lowercase();
        let mut iter1 = ss.chars().filter(|c| c.is_alphanumeric());
        let mut iter2 = ss.chars().filter(|c| c.is_alphanumeric()).rev();
        while let Some(c) = iter1.next() {
            if Some(c) != iter2.next() {
                return false;
            }
        }
        return true;
    }
}