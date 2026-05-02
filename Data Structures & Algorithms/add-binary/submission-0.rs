impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        let al = a.chars().map(|c| c.to_digit(2).unwrap()).rev().collect::<Vec<u32>>();
        let bl = b.chars().map(|c| c.to_digit(2).unwrap()).rev().collect::<Vec<u32>>();
        let n = al.len().max(bl.len());
        let mut ans = Vec::new();
        let mut carry = 0;
        for i in 0..n {
            let l = al.get(i).unwrap_or(&0u32);
            let r = bl.get(i).unwrap_or(&0u32);
            ans.push((l + r + carry) % 2);
            carry = (l + r + carry) / 2
        }
        if carry != 0 {
            ans.push(1);
        }
        ans.iter().map(|x| x.to_string()).rev().collect::<Vec<String>>().join("")
    }
}
