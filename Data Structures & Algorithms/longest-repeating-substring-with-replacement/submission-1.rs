impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        use std::collections::HashMap;
        let s = s.chars().collect::<Vec<char>>();
        let mut l = 0;
        let mut r = 0;
        let mut most = s[0];
        let mut ans = 0;
        let mut map: HashMap<char, i32> = HashMap::new();
        map.insert(most, 1);
        loop {
            if ((r - l + 1) as i32) <= map.get(&most).unwrap() + k {
                ans = ans.max(r - l + 1);
                r += 1;
                if r >= s.len() {
                    break;
                }
                let a = map.entry(s[r as usize]).or_insert(0);
                *a += 1;
                if *a > *map.get(&most).unwrap() {
                    most = s[r as usize];
                }
            } else {
                let a = map.entry(s[l as usize]).or_insert(0);
                *a -= 1;
                l += 1;
                for (key, value) in map.iter() {
                    if value > map.get(&most).unwrap() {
                        most = *key;
                    }
                }
            }

        }
        ans as i32
    }
}
