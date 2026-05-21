impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        let mut five = 0;
        let mut ten = 0;
        let mut twenty = 0;
        for bill in bills {
            match bill {
                5 => five += 1,
                10 => {
                    ten += 1;
                    if five > 0 {
                        five -= 1;
                    } else {
                        return false;
                    }
                },
                20 => {
                    twenty += 1;
                    if ten > 0 && five > 0 {
                        ten -= 1;
                        five -= 1;
                    } else if five >= 3 {
                        five -= 3;
                    } else {
                        return false;
                    }
                },
                _ => {}
            }
        }
        true
    }
}
