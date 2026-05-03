impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        details.iter().filter(|s| Solution::is_old(s)).count() as i32
    }

    fn is_old(s: &str) -> bool {
        let a = s.chars().map(|c| c.to_string()).collect::<Vec<String>>();
        let age: i32 = (a[11].to_owned() + &a[12]).parse::<i32>().unwrap();
        if age > 60 {
            return true;
        } else {
            false
        }
    }
}
