use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct KthLargest {
    heap: BinaryHeap<Reverse<i32>>,
    l: i32
}

impl KthLargest {
    pub fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut ans = Self { heap: BinaryHeap::new(), l: k };
        for num in nums {
            ans.add(num);
        }
        ans
    }

    pub fn add(&mut self, val: i32) -> i32 {
        self.heap.push(Reverse(val));
        if self.heap.len() as i32 > self.l {
            self.heap.pop().unwrap();
        }
        self.heap.peek().unwrap().0
    }
}
