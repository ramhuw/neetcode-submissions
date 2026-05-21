impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        use std::collections::BinaryHeap;
        let mut heap = BinaryHeap::from(stones);
        while let Some(x) = heap.pop() {
            if let Some(y) = heap.pop() {
                if x == y {

                } else {
                    heap.push((y - x).abs());
                }
            } else {
                return x;
            }
        }
        return 0;
    }
}
