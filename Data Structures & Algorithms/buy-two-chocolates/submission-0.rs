impl Solution {
    pub fn buy_choco(prices: Vec<i32>, money: i32) -> i32 {
        let mut v = prices;
        v.sort();
        let a = v[0];
        let b = v[1];
        if a + b <= money {
            return money - a - b;
        } else {
            return money
        }
    }
}
