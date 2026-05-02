use std::collections::HashMap;

impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        let mut maps = HashMap::new();
        let mut mapt = HashMap::new();
        for c in s.chars() {
            let a = maps.entry(c).or_insert(0);
            *a += 1;
        }
        for c in t.chars() {
            let a = mapt.entry(c).or_insert(0);
            *a += 1;
        }
        for (key, value) in mapt.iter() {
            match maps.get(key) {
                None => return *key,
                Some(v) => {
                    if v != value {
                        return *key
                    }
                }
            }
        }
        return ' ';
    }
}
