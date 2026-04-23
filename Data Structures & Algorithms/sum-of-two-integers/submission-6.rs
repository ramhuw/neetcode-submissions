impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        let mut l = a;
        let mut r = b;
        let mut carry = 0;
        while r != 0 {
            carry = l & r;
            l = l ^ r;
            r = carry << 1;
        }
        return l;
    }
}
